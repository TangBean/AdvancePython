from _collections_abc import MutableMapping
import copy


a = {"bean1": {"company": "imooc"},
     "bean2": {"company": "imooc2"}}

# a.clear()

# 浅拷贝，也就是说，字典中的字典只拷贝了一个地址
b = a.copy()
print(b)
b["bean1"]["company"] = "imooc3"
print(b)
print(a)

# 深拷贝
c = copy.deepcopy(a)
c["bean1"]["company"] = "imooc4"
print(c)
print(a)

# fromkeys
new_list = ["bean1", "bean2", "bean3"]
new_dict = dict.fromkeys(new_list, {"company": "imooc"})
print(new_dict)

# setdefault
key = "bean"
print(new_dict.setdefault(key, {"company": "imooc_new"}))
print(new_dict[key])

# update
new_dict.update(bobby="imooc")
new_dict.update([("bobby1", "imooc")])
print(new_dict)
