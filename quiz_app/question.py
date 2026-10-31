"""Задание 1. Реализуй Question по README."""


class Question:
    question_id: str
    text: str
    options: dict

    def __init__(self, question_id: str, text: str, options: dict) -> None:
        self.question_id = question_id
        self.text = text
        self.options = dict(options)

    def as_dict(self) -> dict:
        return {
            "id": self.question_id,
            "text": self.text,
            "options": self.options.copy(),
        }
