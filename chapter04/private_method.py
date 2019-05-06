from chapter04.class_method import Date


class User:
    def __init__(self, birthday):
        self.__birthday = birthday  # __birthday 是一个私有属性

    def get_age(self):
        return 2019 - self.__birthday.year

    def __private_method(self):
        print("I'm private!")


if __name__ == '__main__':
    user = User(Date(1990, 2, 1))
    print(user.get_age())
    print(user._User__birthday)  # 也可以这样偷偷获取，实际上 __birthday 属性的名称被改变了
    user._User__private_method()  # 也可以这样偷偷调用私有方法
