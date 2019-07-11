import glob


def path_to_root(dct, number):
    parent = dct[number]
    if parent == 0:
        return [number]

    return path_to_root(dct, parent) + [number]


def convert(parents):
    children = {0: []}
    for k in parents:
        children[k] = []

    for k in parents:
        val = parents[k]
        children[val].append(k)

    return children


def find_no_children_nodes(parent_to_children):
    res = []
    for k in parent_to_children:
        if parent_to_children[k] == []:
            res.append(k)

    return res

child_to_parent = {}


list_of_files = glob.glob('./files/*.txt')
for f in list_of_files:
    child = f[8:-4]
    parent = open(f).read()

    child = int(child)
    parent = int(parent)

    child_to_parent[child] = parent


parent_to_children = convert(child_to_parent)

print(child_to_parent)
print(parent_to_children)


max_path = []

for node in find_no_children_nodes(parent_to_children):
    path = path_to_root(child_to_parent, node)
    if len(path) > len(max_path):
        max_path = path


print(path_to_root(child_to_parent, 6638932548))

print(max_path)