s = set("abcde")
print(s)

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # False
print(a == b)  # True

a = "abc"
b = "abc"
print(a is b)  # True，Python 也有常量池的概念
print(a == b)  # True
