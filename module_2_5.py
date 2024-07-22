def get_matrix(n, m, value): # Объявите функцию 'get_matrix' и напишите в ней параметры 'n', 'm' и 'value'.
    matrix = [] # Создайте пустой список 'matrix' внутри функции 'get_matrix'.
    for i in range(n): # Напишите первый(внешний) цикл 'for' для кол-ва строк матрицы, 'n' повторов.
        row = [] # В первом цикле добавляйте пустой список в список 'matrix'.
        for j in range(m): # Напишите второй (внутренний) цикл 'for' для кол-ва столбцов матрицы, 'm' повторов.
            row.append(value) # Во втором цикле пополняйте ранее добавленный пустой список значениями 'value'.
        matrix.append(row) # Добавляю заполненную строку в 'м'
    return matrix # После всех циклов верните значение переменной 'matrix'.
# Исходный код
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
# Вывод в консоль
print(result1)
print(result2)
print(result3)