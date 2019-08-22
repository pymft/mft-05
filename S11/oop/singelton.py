class Singleton:
    _singleton = None

    def __new__(cls, *args, **kwargs):
        if cls._singleton is None:
            cls._singleton = super().__new__(cls)
            cls._singleton._is_initiated = False

        return cls._singleton


class OneOnly(Singleton):
    def __init__(self):
        if not self._is_initiated:
            self.f = open("output.txt", mode='a')
            self._is_initiated = True

    def write(self, text):
        self.f.write(text)


for i in range(1000):
    tmp = OneOnly()
    tmp.write(f"tmp {i}\n")
    # print(tmp)
