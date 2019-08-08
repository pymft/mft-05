# class Temperature:
#     def __init__(self, c):
#         self.celsius = c
#
#     @property
#     def fahrenheit(self):
#         return (self.celsius * 1.8) + 32
#
#     # fahrenheit = property(fahrenheit())
#
#     @fahrenheit.setter
#     def fahrenheit(self, value):
#         self.celsius = (self.celsius - 32) * (5/ 9)


class Fahrenheit:
    def __get__(self, instance, owner):
        return (instance.celsius * 1.8) + 32

    def __set__(self, instance, value):
        instance.celsius = (instance.celsius - 32) * (5 / 9)


class Temperature:
    fahrenheit = Fahrenheit()

    def __init__(self, c):
        self.celsius = c


t1 = Temperature(0)
print(t1.celsius, t1.fahrenheit)


t1.fahrenheit = 0
print(t1.celsius, t1.fahrenheit)

