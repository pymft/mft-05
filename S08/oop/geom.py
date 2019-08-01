import math


class Rectangle:
    """
    >>> r = Rectangle(2.0, 5.0)
    >>> r.width
    2.0
    >>> r.height
    5.0
    >>> r.get_area()
    10.0
    >>> r.set_area(40.0)
    >>> r.width
    4.0
    >>> r.height
    10.0
    >>> r.get_perimeter()
    28.0
    >>> r.set_perimeter(7.0)
    >>> r.width
    1.0
    >>> r.height
    2.5
    """

    def __init__(self, w: float, h: float):
        self.width = float(w)
        self.height = float(h)

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def set_area(self, value):
        ratio = math.sqrt(value / self.get_area())
        self.change_ratio(ratio)

    def set_perimeter(self, value):
        ratio = value / self.get_perimeter()
        self.change_ratio(ratio)

    def change_ratio(self, ratio):
        self.width = self.width * ratio
        self.height = self.height * ratio


if __name__ == '__main__':
    import doctest

    doctest.testmod()