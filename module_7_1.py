class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                products = file.readlines()
            return ''.join(products)
        except FileNotFoundError:
            return ''

    def add(self, *products):
        existing_products = self.get_products()
        existing_product_names = set()
        for line in existing_products.split('\n'):
            if line:
                name = line.split(', ')[0]
                existing_product_names.add(name)

        new_product_added = False
        with open(self.__file_name, 'a') as file:
            for product in products:
                if product.name not in existing_product_names:
                    file.write(str(product) + '\n')
                    new_product_added = True
                else:
                    print(f"Продукт {product.name}, {product.weight}, {product.category} уже есть в магазине")


# Пример работы программы:

# Создаём экземпляр Shop
s1 = Shop()

# Создаём объекты Product
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

# Печатаем объект Product, чтобы проверить метод __str__
print(p2)

# Добавляем продукты в магазин
s1.add(p1, p2, p3)

# Получаем и печатаем список всех продуктов в магазине
print(s1.get_products())