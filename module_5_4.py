class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        instance = super(House, cls).__new__(cls)
        cls.houses_history.append(args[0])
        return instance

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(f'Лифт {self.name} поднялся на Этаж {floor}')
        else:
            print(f'В {self.name} такого этажа не существует')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return False

    def demolish(self):
        print(f'{self.name} снесён, но он останется в истории')
        del self


house1 = House('ЖК Эльбрус', 5)
print(House.houses_history)
house2 = House('ЖК Акация', 10)
print(House.houses_history)
house3 = House('ЖК Матрёшки', 8)
print(House.houses_history)

house2.demolish()
house3.demolish()
print(House.houses_history)

house1.demolish()