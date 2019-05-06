from datetime import date, datetime
import numbers


class IntField:
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        # 可以在这里进行类型检查
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        if value < 0:
            raise ValueError("positive value need")
        self.value = value

    def __delete__(self, instance):
        pass


class User:
    age = IntField()

    def __init__(self, info={}):
        self.info = info

    def __getattr__(self, item):
        return self.info[item]

    # def __getattribute__(self, item):
    #     # 访问属性时，无条件进入该函数
    #     print("哈哈哈哈")


if __name__ == '__main__':
    # user = User({"name": "bean", "birthday": date(year=2000, month=1, day=1), "company_name": "imooc"})
    # print(user.birthday)
    user = User()
    user.age = 4
    print(user.age)

    user1 = User()
    user1.age = 5
    print(user1.age)
    print(user.age)
