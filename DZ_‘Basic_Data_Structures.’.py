# Дополнительное практическое задание по модулю: "Базовые структуры данных."

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Строчки с оценками
line_1 = grades[0]
line_2 = grades[1]
line_3 = grades[2]
line_4 = grades[3]
line_5 = grades[4]

# Упорядочить список в множестве
students = sorted(students)

# Перевести множество в словарь
students = dict.fromkeys(students)

# Считаю количество оценок в строках:
len_ = len(line_1), len(line_2), len(line_3), len(line_4), len(line_5)

# Нахожу суммарный бал по каждой строке
sum_ = sum(line_1), sum(line_2), sum(line_3), sum(line_4), sum(line_5)

# Нахожу средний бал
average_score = sum_[0]/len_[0], sum_[1]/len_[1], sum_[2]/len_[2], sum_[3]/len_[3], sum_[4]/len_[4]

# Назначаю ячейки с итоговым результатом
cell_1 = average_score[0]
cell_2 = average_score[1]
cell_3 = average_score[2]
cell_4 = average_score[3]
cell_5 = average_score[4]

# Вписываю имена в алфавитном порядке
students['Aaron'] = cell_1; students['Bilbo'] = cell_2; students['Johnny'] = cell_3
students['Khendrik'] = cell_4; students['Steve'] = cell_5

print(students)
