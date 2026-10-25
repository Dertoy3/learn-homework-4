"""Готовый HTTP-адаптер. Запуск: python -m services.checker.app"""
from pathlib import Path
from common.server import serve
from config import HOST, CHECKER_PORT
from .domain import AnswerChecker

def make_dispatch(service):
    def dispatch(method, path, body):
        if method == "POST" and path == "/check":
            if not isinstance(body, dict) or "answers" not in body:
                raise ValueError("Нужен объект с полем answers")
            return 200, service.check(body["answers"])
        return 404, {"error": "Маршрут не найден"}
    return dispatch

def main():
    service = AnswerChecker(Path(__file__).with_name("answer_key.json"))
    serve(HOST, CHECKER_PORT, "checker", make_dispatch(service))

if __name__ == "__main__":
    main()
