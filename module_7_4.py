# Переменные
team1_num = 5
team2_num = 6

# Форматирование с использованием %
team1_string = "В команде Мастера кода участников: %d ! " % team1_num
all_teams_string = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)

print(team1_string)
print(all_teams_string)

# Переменные
score_2 = 42
team1_time = 18015.2

# Форматирование с использованием .format()
team2_score_string = "Команда Волшебники данных решила задач: {} !".format(score_2)
team2_time_string = "Волшебники данных решили задачи за {:.1f} с !".format(team1_time)

print(team2_score_string)
print(team2_time_string)

# Переменные
score_1 = 40
challenge_result = 'Победа команды Волшебники данных!'
tasks_total = 82
time_avg = 350.4

# Форматирование с использованием f-строк
score_string = f"Команды решили {score_1} и {score_2} задач."
result_string = f"Результат битвы: {challenge_result}"
tasks_string = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!."

print(score_string)
print(result_string)
print(tasks_string)

if score_1 > score_2 or (score_1 == score_2 and team1_time > team2_time_string):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time < team2_time_string):
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

print(f"Результат битвы: {challenge_result}")