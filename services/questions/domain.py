"""ЗАДАНИЕ 1. Контракты в docs/tasks.md. Замени raise своим кодом."""
import json
from pathlib import Path

class Question:
    def __init__(self, question_id, text, options):
        raise NotImplementedError("Реализуй Question.__init__")

    def as_dict(self):
        raise NotImplementedError("Реализуй Question.as_dict")

class QuestionService:
    def __init__(self, path):
        self.path = Path(path)

    def list_questions(self):
        raise NotImplementedError("Реализуй QuestionService.list_questions")
