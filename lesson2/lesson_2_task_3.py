import math


def square(side):
    square = side * side
    print(f"Площадь квадрата {square}")
    return math.ceil(square)


square(8.7)
