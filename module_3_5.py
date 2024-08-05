def get_multiplied_digits(number):
    str_number = str(number) # преобразую число в строку
    # если длина строки не больше 1, возвращаю оставшуюся цифру
    if len(str_number) <= 1:
        return int(str_number)
    # иначе оделить первую цифру
    first = int(str_number[0])
    # рекурсивно умножаю первую цифру на результат для остальных цифр
    return first * get_multiplied_digits(int(str_number[1:]))
# проверяю работоспособность 
result = get_multiplied_digits(40203)
print(result)