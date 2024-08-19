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

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return True

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


dom = House('ЖК "Эльбрус"', 10)
dom_2 = House('ЖК "Ленинский парк"', 20)

print(dom)
print(dom_2)

print(dom == dom_2)
print('|------------------------------------------------------|')
dom = dom + 10
print(dom)
print(dom == dom_2)
print('|------------------------------------------------------|')
dom += 10
print(dom)
print('|------------------------------------------------------|')
dom = 10 + dom_2
print(dom_2)
print('|------------------------------------------------------|')
print(dom > dom_2)
print(dom >= dom_2)
print(dom < dom_2)
print(dom <= dom_2)
print(dom != dom_2)
print('|------------------------------------------------------|')
