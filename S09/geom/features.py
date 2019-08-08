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

