my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
positive_numbers = []
i = 0

while i < len(my_list):
    if my_list[i] > 0:
        positive_numbers.append(my_list[i])
    if my_list[i] >= 0:
        list(filter(lambda x: x > 0, positive_numbers))
    else:
        break
    i += 1

for number in positive_numbers:
    print(number)