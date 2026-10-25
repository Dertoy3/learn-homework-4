"""Готовый HTTP-адаптер. Запуск: python -m services.questions.app"""
from pathlib import Path
from common.server import serve
from config import HOST, QUESTIONS_PORT
from .domain import QuestionService

def make_dispatch(service):
    def dispatch(method, path, body):
        if method == "GET" and path == "/questions":
            return 200, {"questions": service.list_questions()}
        return 404, {"error": "Маршрут не найден"}
    return dispatch

def main():
    service = QuestionService(Path(__file__).with_name("questions.json"))
    serve(HOST, QUESTIONS_PORT, "questions", make_dispatch(service))

if __name__ == "__main__":
    main()
