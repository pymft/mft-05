class Dimension:
    def __init__(self, val):
        if not isinstance(val, (int, float)):
            raise ValueError
        self.val = val


class Vector:
    def __init__(self, *args):
        self.dims = [Dimension(d) for d in args]

    def length(self):
        return (sum([d.val ** 2 for d in self.dims])) ** 0.5


v1 = Vector(4, 3)
# v1.set_vals(4, 3)

v2 = Vector(40, 30)
# v2.set_vals(40, 30)

Vector.length(v1)
v1.length()
print(v1.length())
