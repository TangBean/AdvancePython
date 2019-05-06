from collections.abc import Iterable, Iterator

# 迭代器是一种惰性处理数据的方式

a = [1, 2]
print(isinstance(a, Iterable))  # True
print(isinstance(a, Iterator))  # False

iter_rator = iter(a)
print(isinstance(iter_rator, Iterator))  # True


