# 先看 zip 函数的用途：
# Returns an iterator of tuples, where the i-th tuple contains the i-th
# element from each of the argument sequences or iterables.
result = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
zip_res = zip(*result)
for zr in zip_res:
    print(zr)

# 以上的输出：
# (1, 5, 9)
# (2, 6, 10)
# (3, 7, 11)
# (4, 8, 12)

# 接下来看 map 函数的用途，map(func, *iterable)，map 的效果大概是这样的：
"""
def map(func, *iterable):
    res = []
    for it in iterable:
        res.append(func(it))
    return res
"""

# 最后 tuple 的作用就是将 map 函数返回的结果包装成一个 元组tuple

# 也就是说，tuple(map(list, zip(*result))) 就是：
res = tuple(map(list, zip(*result)))
print(res)  # 输出：([1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12])

# 就是把 zip(*result) 的结果变成一个一个的 list，然后把这些 list 塞进一个 tuple 中

