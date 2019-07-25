# Syntax Error
# Runtime Error
# Logical Error


a = 100
b = 0
lst = [1, 2, 3, 4]
dct = {'a': 1000}

try:
    lst[1000]
except ZeroDivisionError as e:
    print("zero division error")
finally:
    print("finally")

print("hello")
