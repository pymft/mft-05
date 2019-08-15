class NoDuplicate:
    instances = {}

    def __new__(cls, name):
        if name in cls.instances:
            return cls.instances[name]
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name
        self.instances[name] = self

    @classmethod
    def count(cls):
        return len(cls.instances)

    def count2(self):
        return len(self.instances)


print(NoDuplicate.count())
p1 = NoDuplicate("A")
print(p1.count())
print(p1.count2())
print(NoDuplicate.count())
print(NoDuplicate.count2())

