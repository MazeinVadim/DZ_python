import threading
import time
from time import sleep

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

# Взятие текущего времени
start_time = time.time()

# Запуск функций с аргументами из задачи
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Взятие текущего времени
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Работа функций {time.strftime('%H:%M:%S', time.gmtime(elapsed_time))}.{int((elapsed_time % 1) * 1_000_000):06d}")

# Взятие текущего времени
start_time = time.time()

# Создание и запуск потоков с аргументами из задачи
threads = []
threads.append(threading.Thread(target=write_words, args=(10, 'example5.txt')))
threads.append(threading.Thread(target=write_words, args=(30, 'example6.txt')))
threads.append(threading.Thread(target=write_words, args=(200, 'example7.txt')))
threads.append(threading.Thread(target=write_words, args=(100, 'example8.txt')))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

# Взятие текущего времени
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Работа потоков {time.strftime('%H:%M:%S', 
                                      time.gmtime(elapsed_time))}.{int((elapsed_time % 1) * 1_000_000):06d}")