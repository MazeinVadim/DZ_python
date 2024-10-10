import time
import multiprocessing
import os
from datetime import datetime, timedelta

def read_info(name):
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:  # Проверяем, что строка не пустая
                break

if __name__ == '__main__':
    # Список файлов для чтения
    filenames = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt'] 

    # Линейное чтение
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    end_time = time.time()
    elapsed_time_linear = timedelta(seconds=end_time - start_time)
    print(f"{elapsed_time_linear} (линейное)")

    # Многопроцессное чтение
    start_time = time.time()
    with multiprocessing.Pool(processes=os.cpu_count()) as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    elapsed_time_multiprocessing = timedelta(seconds=end_time - start_time)
    print(f"{elapsed_time_multiprocessing} (многопроцессное)")
