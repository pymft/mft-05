import math


class InvalidTriangleEdgeTypesError(TypeError):
    pass


class NotATriangleError(ValueError):
    pass


def is_triangle(a, b, c) -> bool:
    if not (isinstance(a, (int, float)) and
            isinstance(b, (int, float)) and
            isinstance(c, (int, float))):
        raise InvalidTriangleEdgeTypesError("message")

    if a < b + c and b < a + c and c < a + b:
        return True
    return False


def type_of_triangle(a, b, c):
    if not is_triangle(a, b, c):
        raise NotATriangleError("a, b, c doesn't create a triangle")

    x = a ** 2 + b ** 2 + c ** 2
    y = 2 * max(a, b, c) ** 2
    if math.isclose(x, y):
        print("right")

    x = len({a, b, c})
    if x == 1:
        print("Equilateral ")
    elif x == 2:
        print("Isosceles")


type_of_triangle(3, 3, 3 * (2 ** 0.5))
