"""Готовые контрактные тесты. Они падают, пока методы являются заглушками."""
import copy
import json
from pathlib import Path
import tempfile
import threading
import unittest
from common.client import ClientError, request_json
from common.server import create_server
from services.questions.domain import QuestionService
from services.checker.domain import AnswerChecker
from services.reports.domain import ReportStore
from services.questions.app import make_dispatch

ROOT = Path(__file__).resolve().parents[1]

class ContractTests(unittest.TestCase):
    def test_questions(self):
        questions = QuestionService(ROOT / "services/questions/questions.json").list_questions()
        self.assertEqual([q["id"] for q in questions], ["q1", "q2"])
        self.assertNotIn("correct", questions[0])
        self.assertEqual(questions[0]["options"]["B"], "dict")

    def test_checker(self):
        checker = AnswerChecker(ROOT / "services/checker/answer_key.json")
        answers = {"q1": "B", "q2": "A"}
        before = copy.deepcopy(answers)
        self.assertEqual(checker.check(answers), {"correct": 2, "total": 2, "percent": 100.0})
        self.assertEqual(answers, before)
        self.assertEqual(checker.check({}), {"correct": 0, "total": 2, "percent": 0.0})
        with self.assertRaises(ValueError):
            checker.check({"unknown": "B"})
        with self.assertRaises(ValueError):
            checker.check({"q1": "Z"})

    def test_reports(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "reports.json"
            store = ReportStore(path)
            self.assertEqual(store.list_reports(), [])
            result = {"correct": 1, "total": 2, "percent": 50.0}
            report = store.save(result)
            self.assertTrue(report["id"])
            self.assertEqual(report["result"], result)
            result["correct"] = 2
            self.assertEqual(report["result"]["correct"], 1)
            self.assertEqual(len(store.list_reports()), 1)

    def test_damaged_storage(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "broken.json"
            path.write_text("{", encoding="utf-8")
            with self.assertRaises(json.JSONDecodeError):
                ReportStore(path).list_reports()

    def test_http(self):
        service = QuestionService(ROOT / "services/questions/questions.json")
        server = create_server("127.0.0.1", 0, "questions", make_dispatch(service))
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        url = f"http://127.0.0.1:{server.server_port}"
        try:
            self.assertEqual(request_json("GET", url + "/health")["status"], "ok")
            self.assertEqual(len(request_json("GET", url + "/questions")["questions"]), 2)
            with self.assertRaises(ClientError):
                request_json("GET", url + "/unknown")
        finally:
            server.shutdown()
            server.server_close()
            thread.join()
