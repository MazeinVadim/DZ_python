def add_everything_up(a, b):
    try:
        # Проверяем, если оба аргумента числа (int или float)
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        # Проверяем, если оба аргумента строки
        elif isinstance(a, str) and isinstance(b, str):
            return a + b
        # Если аргументы разных типов
        else:
            raise TypeError
    except TypeError:
        # Возвращаем строковое представление обоих аргументов
        return f"{a}{b}"

# Примеры использования
print(add_everything_up(123.456, 'строка'))  # Вывод: 123.456строка
print(add_everything_up('яблоко', 4215))    # Вывод: яблоко4215
print(add_everything_up(123.456, 7))        # Вывод: 130.456