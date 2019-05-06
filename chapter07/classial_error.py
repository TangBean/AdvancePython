class Company:
    def __init__(self, name, staffs=[]):
        self.name = name
        self.staffs = staffs

    def add(self, staff):
        self.staffs.append(staff)

    def __str__(self):
        return "%s: %s" % (self.name, self.staffs)


com1 = Company("com1", ["bean1", "bean2"])
com1.add("bean")
print(com1)  # com1: ['bean1', 'bean2', 'bean']

com2 = Company("com2")
com2.add("bean2")
com2.add("bean22")
print(com2)  # com2: ['bean2', 'bean22']

com3 = Company("com3")
com3.add("bean3")
com3.add("bean33")
print(com3)  # com3: ['bean2', 'bean22', 'bean3', 'bean33']

# 因为 com2 和 com3 的 staffs list 用的都是默认的 []，本质上是一个对象
print(com2.staffs is com1.staffs)  # False
print(com2.staffs is com3.staffs)  # True
