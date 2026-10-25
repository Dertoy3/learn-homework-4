"""ЗАДАНИЕ 2. Реализуй проверку, не меняя входной словарь."""
import json
from pathlib import Path

class AnswerChecker:
    def __init__(self, path):
        self.path = Path(path)

    def check(self, answers):
        raise NotImplementedError("Реализуй AnswerChecker.check")
