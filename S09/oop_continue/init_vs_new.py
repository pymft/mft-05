class A:
    instances = {}

    def __new__(cls, name):
        if name in cls.instances:
            return cls.instances[name]
        return super().__new__(cls)

    def __init__(self, name):
        self.instances[name] = self


a = A("alex")
print(a, a.instances)
a = A("allen")
print(a, a.instances)
a = A("alex")
print(a, a.instances)