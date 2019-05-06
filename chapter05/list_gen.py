"""
列表生成式
"""
# 提取 1~20 之间的奇数
odd_list = [i for i in range(21) if i % 2 == 1]
print(odd_list)


# 逻辑复杂的情况
def handle_item(item):
    return item * item


# 列表生成式的性能高于列表操作
square_list = [handle_item(i) for i in range(21) if i % 2 == 1]
print(square_list)


"""
生成器表达式
"""
odd_list = (i for i in range(21) if i % 2 == 1)
print(type(odd_list))
for item in odd_list:
    print(item)


"""
字典推导式
"""
my_dict = {"bean1": 22, "bean2": 23, "bean3": 5}
reversed_dic = {value: key for key, value in my_dict.items()}
print(type(my_dict))
print(reversed_dic)


"""
集合推导式
"""
my_set = {key for key, value in my_dict.items()}
print(type(my_set))
print(my_set)
