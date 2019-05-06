

def say(self):
    return self.name


class MetaClass(type):
    def __init__(cls, name, base, attrs):
        return super().__init__(name, base, attrs)


class User(metaclass=MetaClass):
    pass


if __name__ == '__main__':
    # type(name, bases, dict)
    # - name：类名
    # - bases：基类
    # - dict：类的属性
    # User = type("User", (), {"name": "user", "say": say})
    # user = User()
    # print(user.name)
    # print(user.say())

    user = User()
    print(user)
