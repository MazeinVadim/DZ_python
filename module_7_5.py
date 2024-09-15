import os
import time

# Указываем директорию, которую будем обходить
directory = "module_7"

# Обходим файловую систему с помощью os.walk
for root, dirs, files in os.walk(directory):
    for file in files:
        # Формируем полный путь к файлу
        filepath = os.path.join(root, file)

        # Получаем время последнего изменения файла
        filetime = os.path.getmtime(filepath)

        # Форматируем время в более читабельный формат
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        # Получаем размер файла в байтах
        filesize = os.path.getsize(filepath)

        # Получаем родительскую директорию файла
        parent_dir = os.path.dirname(filepath)

        # Выводим информацию о файле
        print(
            f'Обнаружен файл: {file}, '
            f'Путь: {filepath}, '
            f'Размер: {filesize} байт, '
            f'Время изменения: {formatted_time}, '
            f'Родительская директория: {parent_dir}'
        )