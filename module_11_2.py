def introspection_info(obj):
    # Определение типа объекта
    obj_type = type(obj).__name__

    # Получение атрибутов объекта
    attributes = dir(obj)

    # Получение методов объекта
    methods = [method for method in attributes if callable(getattr(obj, method))]

    # Определение модуля, к которому объект принадлежит
    module = obj.__class__.__module__

    # Создание словаря с информацией об объекте
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module
    }

    return info


# Пример использования функции
number_info = introspection_info(42)
print(number_info)

string_info = introspection_info("Hello")
print(string_info)

list_info = introspection_info([1, 2, 3])
print(list_info)