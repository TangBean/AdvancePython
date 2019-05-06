class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    # 有了这个函数我们就可以迭代 Company 对象了
    def __getitem__(self, item):
        return self.employee[item]


company = Company(['tom', 'bob', 'jane'])

for em in company:
    print(em)
