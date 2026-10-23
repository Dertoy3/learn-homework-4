"""Готовые проверки задания 8. Используют только временные файлы."""
import json
from pathlib import Path
import tempfile
import unittest
from plantbook.models import Plant
from plantbook.storage import load_plants, save_plants

class GardenTests(unittest.TestCase):
    def test_missing(self):
        with tempfile.TemporaryDirectory() as folder:
            self.assertEqual(load_plants(Path(folder) / "missing.json"), [])

    def test_round_trip(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "garden.json"
            save_plants(path, [Plant("Алоэ", 2)])
            restored = load_plants(path)
            self.assertIsInstance(restored[0], Plant)
            self.assertEqual(restored[0].as_dict(), {"name": "Алоэ", "water_count": 2})

    def test_broken_json(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "broken.json"
            path.write_text("{", encoding="utf-8")
            with self.assertRaises(json.JSONDecodeError):
                load_plants(path)

    def test_water(self):
        plant = Plant("Фикус")
        self.assertEqual(plant.water(2), 2)
        with self.assertRaises(ValueError):
            plant.water(0)
        self.assertEqual(plant.water_count, 2)
