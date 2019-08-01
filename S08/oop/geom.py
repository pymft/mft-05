import math


class Rectangle:
    def __init__(self, w: float, h: float):
        print("hi from rectangle")
        self.width = float(w)
        self.height = float(h)

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

    def change_ratio(self, ratio):
        self.width *= ratio
        self.height *= ratio

    @area.setter
    def area(self, value):
        ratio = math.sqrt(value / self.area)
        self.change_ratio(ratio)

    @perimeter.setter
    def perimeter(self, value):
        ratio = value / self.perimeter
        self.change_ratio(ratio)


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)


r = Rectangle(2.0, 5.0)
print(r.width, r.height, r.area, r.perimeter)

r.area = 40.0
print(r.width, r.height, r.area, r.perimeter)



