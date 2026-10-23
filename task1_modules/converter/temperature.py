"""Задание 1. Реализуй функции пакета converter. Не округляй результат."""

def celsius_to_fahrenheit(value):
    'Формула: value * 9 / 5 + 32. Для 0 верни 32.0, для 100 верни 212.0.'
    pass

def fahrenheit_to_celsius(value):
    'Формула: (value - 32) * 5 / 9. Для 32 верни 0.0, для 212 верни 100.0.'
    pass

def main():
    print("0 C:", celsius_to_fahrenheit(0))
    print("32 F:", fahrenheit_to_celsius(32))

if __name__ == "__main__":
    main()
