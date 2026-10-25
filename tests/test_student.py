"""ЗАДАНИЕ 4. Удали skip и замени тело каждого метода настоящим тестом."""
from pathlib import Path
import tempfile
import unittest
from services.questions.domain import Question
from services.reports.domain import ReportStore

class StudentTests(unittest.TestCase):
    @unittest.skip("Напиши проверку копирования options")
    def test_options_copy(self):
        pass

    @unittest.skip("Напиши проверку чтения после создания нового хранилища")
    def test_new_store_reads_history(self):
        pass

    @unittest.skip("Напиши проверку сохранности файла после неверного result")
    def test_invalid_result_preserves_file(self):
        pass
