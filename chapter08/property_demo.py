from datetime import datetime, date


class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    @property
    def age(self):
        """
        通过取属性的方式调用函数
        """
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self, val):
        self._age = val


if __name__ == '__main__':
    # 测试代码尽量写在 __main__ 函数中，否则 import 会执行
    user = User("bean", date(year=2000, month=1, day=1))
    print(user.age)
    user._age = 30
    print(user._age)
