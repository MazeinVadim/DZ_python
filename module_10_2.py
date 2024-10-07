import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.days = 0

    def run(self):
        enemies = 100
        print(f"{self.name}, на нас напали!")
        while enemies > 0:
            time.sleep(1)
            self.days += 1
            enemies -= self.power
            if enemies > 0:
                print(f"{self.name} сражается {self.days} день(дня)..., осталось {enemies} воинов.")
            else:
                enemies = 0
                print(f"{self.name} сражается {self.days} день(дня)..., осталось {enemies} воинов.")
                print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")
                break

# Создание рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения потоков
first_knight.join()
second_knight.join()

print("Все битвы закончились!")