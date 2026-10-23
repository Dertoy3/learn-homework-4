"""
Задание 5. Исключения и отладка.
parse_count получает строку. average получает список чисел.
В average ниже намеренно допущена логическая ошибка.
До исправления запиши в комментарии ожидание для [4, 6] и [5].
Исправь формулу и отдельно обработай [] возвратом None.
"""

def parse_count(text):
    'Верни int(text). Если результат отрицательный, вызови ValueError. Нечисловая строка тоже должна приводить к ValueError.'
    pass

def average(values):
    'Верни среднее арифметическое. Для [] верни None.'
    return sum(values) / (len(values) - 1)

def main():
    for text in ["3", "0", "-2", "много"]:
        try:
            print(text, parse_count(text))
        except ValueError as error:
            print(text, "Ошибка:", error)
    for values in [[4, 6], [5], []]:
        try:
            print(values, average(values))
        except ZeroDivisionError as error:
            print("Ошибка в average:", error)

if __name__ == "__main__":
    main()
