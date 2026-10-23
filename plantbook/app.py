"""Запуск из корня: python -m plantbook.app"""
from pathlib import Path
from .models import Plant
from .storage import load_plants, save_plants

def main():
    base = Path(__file__).resolve().parent.parent
    path = base / "work_results" / "garden.json"
    path.parent.mkdir(exist_ok=True)
    plants = load_plants(path)
    if not plants:
        plants = [Plant("Фикус")]
    plants[0].water()
    save_plants(path, plants)
    for plant in plants:
        print(plant.as_dict())

if __name__ == "__main__":
    main()
