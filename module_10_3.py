import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            with self.condition:
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance}")
                if self.balance >= 500:
                    self.condition.notify_all()
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            print(f"Запрос на {amount}")
            with self.condition:
                while amount > self.balance:
                    print("Запрос отклонён, недостаточно средств")
                    self.condition.wait()
                self.balance -= amount
                print(f"Снятие: {amount}. Баланс: {self.balance}")
            time.sleep(0.001)

bk = Bank()

# Создание потоков для методов deposit и take
th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

# Запуск потоков
th1.start()
th2.start()

# Ожидание завершения потоков
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')