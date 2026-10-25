"""Общие настройки запуска. Чужие файлы данных здесь не читаются."""
import os

HOST = "127.0.0.1"
QUESTIONS_PORT = int(os.environ.get("QUESTIONS_PORT", "8101"))
CHECKER_PORT = int(os.environ.get("CHECKER_PORT", "8102"))
REPORTS_PORT = int(os.environ.get("REPORTS_PORT", "8103"))
QUESTIONS_URL = f"http://{HOST}:{QUESTIONS_PORT}"
CHECKER_URL = f"http://{HOST}:{CHECKER_PORT}"
REPORTS_URL = f"http://{HOST}:{REPORTS_PORT}"
