class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


v1 = Vector(4, 3)
# v1.set_vals(4, 3)

v2 = Vector(40, 30)
# v2.set_vals(40, 30)

Vector.length(v1)
v1.length()
print(v1.length())
