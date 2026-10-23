"""
Задание 4. JSON. Используй UTF-8, ensure_ascii=False и indent=2.
Для отсутствующего файла верни [], для повреждённого JSON сохрани JSONDecodeError.
В этом упражнении считаем, что корректный JSON содержит список словарей.
"""

import json
from pathlib import Path

def save_records(path, records):
    'Запиши список словарей в JSON. Родительская папка существует. Верни None.'
    pass

def load_records(path):
    'Прочитай и верни данные. Обработай только FileNotFoundError возвратом [].'
    pass

def main():
    base = Path(__file__).resolve().parent
    path = base / "work_results" / "shopping.json"
    path.parent.mkdir(exist_ok=True)
    records = [{"item": "тетрадь", "quantity": 3}]
    save_records(path, records)
    print("Из файла:", load_records(path))

if __name__ == "__main__":
    main()
