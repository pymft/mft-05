import numpy as np

arr1 = np.zeros((7, 7))
arr2 = np.ones((5, 5))

arr1[1:-1, 1:-1] = arr2

print(arr1)
