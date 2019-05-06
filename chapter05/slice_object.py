import numbers
from _collections_abc import Sequence


class Group(Sequence):
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __str__(self):
        return self.staffs.__str__()

    def __reversed__(self):
        self.staffs.reverse()

    # 关键，实现它就可以进行切片了，是 @abstractmethod
    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=self.staffs[index])
        elif isinstance(index, numbers.Integral):
            # index 是一个数，需要把它包装成 list
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=[self.staffs[index]])

    def __contains__(self, value):
        if value in self.staffs:
            return True
        else:
            return False

    def __iter__(self):
        return iter(self.staffs)

    def __len__(self):
        return len(staffs)


if __name__ == '__main__':
    staffs = ["bean1", "bean2", "bean3", "bean4"]
    group = Group(company_name="imooc", group_name="user", staffs=staffs)
    sub_group = group[:2]
    print(sub_group)

    print(len(group))

    if "bean1" in group:
        print("Yes")

    reversed(group)
    for g in group:
        print(g)
