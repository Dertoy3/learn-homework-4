"""Задание 7. Напиши четыре теста готовой функции initials.
Вход — список непустых строк. Пустой список допустим.
Тесты: два слова, одно слово, пустой список, буквы разного регистра.
Пример: ["красный", "дуб"] даёт "КД".
Не изменяй text_tools.py. Ниже один демонстрационный тест.
В четырёх остальных методах замени pass проверками assertEqual.
"""
import unittest
from text_tools import initials

class InitialsTests(unittest.TestCase):
    def test_example(self):
        self.assertEqual(initials(["красный", "дуб"]), "КД")

    def test_two_words(self):
        pass

    def test_one_word(self):
        pass

    def test_empty(self):
        pass

    def test_mixed_case(self):
        pass
