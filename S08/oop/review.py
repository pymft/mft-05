class Tree:
    name = "derakht"

    def __init__(self, name,  h):
        self.height = h
        self.name = name


    def get_height(self):
        return self.height



obj_1 = Tree("maple", 100)
res = obj_1.get_height()
print(res)


# Tree.get_height(obj_1)
# obj_1.get_height()


obj_2 = Tree("oak", 50)
res = obj_2.get_height()
res = Tree.get_height(obj_2)
print(res)






