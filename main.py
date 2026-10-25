"""Общий координатор: общается с сервисами только через HTTP."""
import argparse
import json
from pathlib import Path
from common.client import ClientError, request_json
from config import QUESTIONS_URL, CHECKER_URL, REPORTS_URL

def run_quiz(answers, questions_url=QUESTIONS_URL, checker_url=CHECKER_URL, reports_url=REPORTS_URL):
    questions = request_json("GET", questions_url + "/questions")["questions"]
    print(f"Получено вопросов: {len(questions)}")
    for question in questions:
        print(question["id"], question["text"], question["options"])
    result = request_json("POST", checker_url + "/check", {"answers": answers})
    report = request_json("POST", reports_url + "/reports", {"result": result})["report"]
    print(f"Верно: {result['correct']} из {result['total']}, {result['percent']}%")
    print("Отчёт сохранён:", report["id"])
    return report

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--answers", type=Path, default=Path(__file__).with_name("demo_answers.json"))
    args = parser.parse_args()
    try:
        with args.answers.open(encoding="utf-8") as file:
            answers = json.load(file)
        run_quiz(answers)
    except (ClientError, OSError, ValueError, KeyError, TypeError) as error:
        print("Ошибка сценария:", error)
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
