"""Задание 2. Загрузка вопросов и проверка ответов."""
import json
from pathlib import Path
from .question import Question

class Quiz:
    def __init__(self, questions_path, answer_key_path):
        self.questions_path = Path(questions_path)
        self.answer_key_path = Path(answer_key_path)

    def load_questions(self):
        raise NotImplementedError("Реализуй Quiz.load_questions")

    def check_answers(self, answers):
        raise NotImplementedError("Реализуй Quiz.check_answers")
