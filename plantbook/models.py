"""
Задание 6. Класс Plant.
name — непустая строка, water_count — целое число >= 0.
Считай входные типы корректными. Отрицательный water_count вызывает ValueError.
water(amount) увеличивает счётчик на целое amount > 0 и возвращает новый счётчик.
Если amount <= 0, вызывай ValueError и сохраняй прежнее состояние.
as_dict() возвращает новый словарь с ключами name и water_count.
Счётчики двух экземпляров независимы.
"""
class Plant:
    def __init__(self, name, water_count=0):
        pass

    def water(self, amount=1):
        pass

    def as_dict(self):
        pass
