import math

class Figure:
    def __init__(self, color, sides_count, *sides):
        self.sides_count = sides_count
        self.__sides = sides if self.__is_valid_sides(*sides) else [1] * self.sides_count
        self.__color = color if self.__is_valid_color(*color) else [0, 0, 0]
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255
        return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        if len(sides) == self.sides_count:
            return all(isinstance(side, int) and side > 0 for side in sides)
        return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides

class Circle(Figure):
    def __init__(self, color, *sides):
        sides_count = 1
        super().__init__(color, sides_count, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    def __init__(self, color, *sides):
        sides_count = 3
        super().__init__(color, sides_count, *sides)

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    def __init__(self, color, *sides):
        sides_count = 12
        sides = sides * 12 if len(sides) == 1 else [1] * sides_count
        if len(sides) != sides_count:
            sides = [1] * sides_count
        super().__init__(color, sides_count, *sides)

    def get_volume(self):
        side_length = self.get_sides()[0]
        return side_length ** 3

circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)


circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())