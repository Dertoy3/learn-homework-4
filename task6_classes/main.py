"""После реализации ожидаются счётчики 3 и 0."""
from plant import Plant

def main():
    first = Plant("Фикус")
    second = Plant("Алоэ")
    print(first.water())
    print(first.water(2))
    print(first.as_dict())
    print(second.as_dict())
    try:
        first.water(0)
    except ValueError as error:
        print("Ошибка:", error)

if __name__ == "__main__":
    main()
