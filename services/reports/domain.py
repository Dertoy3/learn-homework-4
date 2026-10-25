"""ЗАДАНИЕ 3. Реализуй хранение истории. Контракт в docs/tasks.md."""
import json
from pathlib import Path
import uuid

class ReportStore:
    def __init__(self, path):
        self.path = Path(path)

    def list_reports(self):
        raise NotImplementedError("Реализуй ReportStore.list_reports")

    def save(self, result):
        raise NotImplementedError("Реализуй ReportStore.save")
