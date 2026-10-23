"""
Задание 3. Текстовые файлы. Данные находятся в samples/supplies.txt.
Работай с UTF-8 и with. Не перехватывай ошибку отсутствующего файла.
Для образца ожидается ["бумага", "ручки", "скотч"].
"""

from pathlib import Path

def read_items(path):
    'Верни список непустых строк после strip(). Для пустого файла верни [].'
    pass

def write_items(path, items):
    'Перезапиши файл: один элемент на строку, после каждого — перенос. Родительская папка уже существует. Верни число записанных элементов. Для [] создай пустой файл и верни 0.'
    pass

def main():
    base = Path(__file__).resolve().parent
    source = base / "samples" / "supplies.txt"
    target = base / "work_results" / "clean.txt"
    target.parent.mkdir(exist_ok=True)
    print("Список:", read_items(source))
    print("Запись:", write_items(target, ["бумага", "ручки"]))
    print("Повторное чтение:", read_items(target))

if __name__ == "__main__":
    main()
