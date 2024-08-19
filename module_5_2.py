class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(f'Лифт {self.name} поднялся на Этаж {floor}')
        else:
            print(f'"В {self.name} такого этажа не существует"')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

dom = House('ЖК "Эльбрус"', 10)
dom_2 = House('ЖК "Ленинский парк"', 20)


dom.go_to(5)
dom.go_to(31)
print('|------------------------------------------------------|')
dom_2.go_to(7)
dom_2.go_to(21)
print('|------------------------------------------------------|')
print(str(dom))
print(str(dom_2))

print(f'Количество этажей у {dom.name}: {len(dom)}')
print(f'Количество этажей у {dom_2.name}: {len(dom_2)}')


