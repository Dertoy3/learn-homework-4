"""Готовый общий main. Вызывает классы из соседних модулей."""

import json
from pathlib import Path
from quiz_app.quiz import Quiz
from quiz_app.storage import ResultStorage


def main():
    base = Path(__file__).resolve().parent
    quiz = Quiz(base / "data/questions.json", base / "data/answer_key.json")
    storage = ResultStorage(base / "work_results/results.json")
    try:
        questions = quiz.load_questions()
        for question in questions:
            print(question.as_dict())
        with (base / "data/demo_answers.json").open(encoding="utf-8") as file:
            answers = json.load(file)
        result = quiz.check_answers(answers)
        storage.save(result)
        print(f"Верно: {result['correct']} из {result['total']}")
        print("Процент:", result["percent"])
        print("Результатов в истории:", len(storage.load()))
    except NotImplementedError as error:
        print("Задание пока не выполнено:", error)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
