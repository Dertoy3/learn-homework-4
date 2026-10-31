"""Задание 2. Загрузка вопросов и проверка ответов."""

import json
from pathlib import Path
from quiz_app.question import Question


class Quiz:
    def __init__(self, questions_path, answer_key_path):
        self.questions_path = Path(questions_path)
        self.answer_key_path = Path(answer_key_path)

    def load_questions(self) -> list[Question]:
        with open(encoding="utf-8", file=self.questions_path, mode="r") as file:
            dicts: list = json.load(file)
            questions = []

            if not isinstance(dicts, list):
                print("Не правильный формат файла")
                raise Exception

            for d in dicts:
                questions.append(
                    Question(
                        question_id=d.get("id"),
                        text=d.get("text"),
                        options=d.get("options"),
                    )
                )
        return questions

    def check_answers(self, user_answers: dict[str, str]) -> dict:
        with open(encoding="utf-8", file=self.answer_key_path, mode="r") as file:
            correct_answers: dict[str, str] = json.load(file)

        total = 0
        correct = 0

        for ans_id, ans in user_answers.items():
            total += 1
            if ans.lower() == correct_answers.get(ans_id, "").lower():
                correct += 1
        if correct == 0:
            return {"correct": correct, "total": total, "percent": 0.0}
        return {
            "correct": correct,
            "total": total,
            "percent": round(total / correct * 100, 1),
        }


if __name__ == "__main__":
    base = Path(__file__).resolve().parent.parent
    quiz = Quiz(base / "data/questions.json", base / "data/answer_key.json")
    print(type(quiz.load_questions()))
