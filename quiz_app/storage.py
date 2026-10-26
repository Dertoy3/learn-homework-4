"""Задание 3. Хранение списка результатов."""
import json
from pathlib import Path

class ResultStorage:
    def __init__(self, path):
        self.path = Path(path)

    def load(self):
        raise NotImplementedError("Реализуй ResultStorage.load")

    def save(self, result):
        raise NotImplementedError("Реализуй ResultStorage.save")
