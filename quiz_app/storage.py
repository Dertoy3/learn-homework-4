"""Задание 3. Хранение списка результатов."""

import json
from os import mkdir
from pathlib import Path


class ResultStorage:
    def __init__(self, path):
        self.path = Path(path)

    def load(self) -> list:
        try:
            with open(file=self.path, mode="r", encoding="utf-8") as f:
                file: list = json.load(f)
        except FileNotFoundError:
            return []
        return file

    def save(self, result: dict) -> None:
        results = self.load()
        if not self.path.resolve().parent.is_dir():
            mkdir("work_results")
        results.append(result)
        with open(file=self.path, mode="w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        return None
