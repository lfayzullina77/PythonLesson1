import math


def square(items):
    return math.ceil(items * items)


num_items = float(input("ВВведите длину стороны квадрата: "))
print(f"Округленная в большую сторону площадь квадрата: {square(num_items)}")
