"""Готовая функция для задания на тестирование. Реализацию менять не нужно."""
def initials(words):
    if not words:
        return ""
    return "".join(word[0].upper() for word in words)
