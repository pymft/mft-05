# class Person:
#     def __init__(self, name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, value):
#         self.__name = value
#
#     name = property(get_name, set_name)

#
# class Person:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         self.__name = value


class Name:
    def __get__(self, instance, owner):
        return instance.__name

    def __set__(self, instance, value):
        instance.__name = value


class Person:
    name = Name()

    def __init__(self, name):
        self.__name = name



if __name__ == '__main__':
    p1 = Person("Jack")
    print(p1.name)
    p1.name = "Some New Name"
    print(p1.name)

