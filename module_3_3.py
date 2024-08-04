# Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


# вызов функции без аргументов
print_params()
# вызов с одним аргументом
print_params(b=25)  # вызов "print_params(b = 25)" работает
# Вызов с двумя аргументами
print_params(c=[1, 2, 3], b=25)  # вызов "print_params(c=[1,2,3])" работает
# Вызов с тремя аргументами
print_params(6, "'Привет, друг'", False)

# Распаковка параметров:
values_list = [42, 'Vadim', False]
values_dict = {'a': 10, 'b': 'Zahar', 'c': [4, 5, 6]}

# вызов функции с распаковкой параметров
print_params(*values_list)
print_params(**values_dict)

# распаковка с отдельными параметрами
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
