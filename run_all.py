"""Готовый запуск трёх процессов, ожидание /health, запуск main и очистка."""
import subprocess
import sys
import time
from pathlib import Path
from common.client import ClientError, request_json
from config import QUESTIONS_URL, CHECKER_URL, REPORTS_URL

def main():
    root = Path(__file__).resolve().parent
    modules = ["services.questions.app", "services.checker.app", "services.reports.app"]
    urls = [QUESTIONS_URL, CHECKER_URL, REPORTS_URL]
    processes = []
    try:
        # Не используем уже занятые порты чужих процессов.
        for url in urls:
            try:
                request_json("GET", url + "/health", timeout=0.3)
            except ClientError:
                continue
            raise RuntimeError(f"Порт уже отвечает: {url}. Останови ручной запуск или смени порт.")
        for module in modules:
            processes.append(subprocess.Popen([sys.executable, "-m", module], cwd=root))
        for process, url in zip(processes, urls):
            deadline = time.monotonic() + 10
            while True:
                if process.poll() is not None:
                    raise RuntimeError(f"Сервис завершился при старте: {url}")
                try:
                    request_json("GET", url + "/health", timeout=0.3)
                    break
                except ClientError:
                    if time.monotonic() >= deadline:
                        raise RuntimeError(f"Сервис не запустился: {url}")
                    time.sleep(0.1)
        return subprocess.run([sys.executable, "main.py"], cwd=root).returncode
    except (RuntimeError, OSError) as error:
        print("Ошибка запуска:", error)
        return 1
    except KeyboardInterrupt:
        return 130
    finally:
        for process in processes:
            if process.poll() is None:
                process.terminate()
        for process in processes:
            try:
                process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()

if __name__ == "__main__":
    raise SystemExit(main())
