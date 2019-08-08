import math
PI = 3.14


class Area:
    def __get__(self, instance, owner):
        if isinstance(instance, Paralleogram):
            angle = math.radians(instance.alpha)
            coef = math.sin(angle)
            return instance.a * instance.b * coef

        elif isinstance(instance, Circle):
            return PI * instance.radius ** 2

    def __set__(self, instance, value):
        ratio = value / instance.area
        ratio = ratio ** 0.5
        if isinstance(instance, Paralleogram):
            instance.a *= ratio
            instance.b *= ratio
        elif isinstance(instance, Circle):
            instance.radius *= ratio


class Perimeter:
    def __get__(self, instance, owner):
        if isinstance(instance, Paralleogram):
            return 2 * (instance.a + instance.b)
        elif isinstance(instance, Circle):
            return 2 * PI * instance.radius

    def __set__(self, instance, value):
        ratio = value / instance.perimeter
        if isinstance(instance, Paralleogram):
            instance.a *= ratio
            instance.b *= ratio
        elif isinstance(instance, Circle):
            instance.radius *= ratio


class GenericGeometry:
    area = Area()
    perimeter = Perimeter()


class Circle(GenericGeometry):
    def __init__(self, r):
        self.radius = r


class Paralleogram(GenericGeometry):
    def __init__(self, a, b, alpha):
        self.a = a
        self.b = b
        self.alpha = alpha


class Rectangle(Paralleogram):
    """
    >>> r = Rectangle(2.0, 5.0)
    >>> r.height
    5.0
    >>> r.perimeter
    14.0
    >>> r.area = 40.0
    >>> r.width
    4.0
    """

    def __init__(self, w, h):
        super().__init__(w, h, 90)

    @property
    def width(self):
        return self.a

    @property
    def height(self):
        return self.b


class Square(Rectangle):
    """
    >>> s = Square(2.0)
    >>> s.area
    4.0
    >>> s.perimeter = 16.0
    >>> s.area
    16.0
    >>> s.side
    4.0
    """

    def __init__(self, a):
        super().__init__(a, a)

    @property
    def side(self):
        return self.width


if __name__ == '__main__':
    import doctest

    doctest.testmod()
