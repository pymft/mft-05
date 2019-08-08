class Area:
    def __get__(self, instance, owner):
        # if isinstance(instance, Square):
        if owner == Square:
            return instance.side ** 2
        if owner == Circle:
            return 3.1415 * instance.radius ** 2


class GenericGeometry:
    area = Area()
    perimeter = Perimeter()


class Square(Rectangle):
    def __init__(self, a):
        self.side = a


class Circle(GenericGeometry):
    def __init__(self, r):
        self.radius = r