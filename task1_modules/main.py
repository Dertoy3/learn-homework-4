"""Задание 1. Запусти этот файл. Импорты уже настроены.
После реализации функций добавь проверку температуры -40 в обеих шкалах.
В комментарии объясни отличие модуля от пакета.
"""
from converter.temperature import celsius_to_fahrenheit, fahrenheit_to_celsius

def main():
    print("0 C в F:", celsius_to_fahrenheit(0))
    print("100 C в F:", celsius_to_fahrenheit(100))
    print("32 F в C:", fahrenheit_to_celsius(32))

if __name__ == "__main__":
    main()
