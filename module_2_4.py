numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for number in numbers:
    is_prime = True
    if number < 2: # Эта строка устанавливает, что любое число меньше 2 (включая 1) не является простым.
        is_prime = False
    else:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)
print("Primes:", primes) # вывожу на экран простые числа
print("Not Primes:", not_primes) # вывожу на экран не простые числа