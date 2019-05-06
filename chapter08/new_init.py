class User:
    def __new__(cls, *args, **kwargs):
        # 可以自定义类的生成过程
        # 执行于 init 方法前
        print("In new")
        return super().__new__(cls)

    def __init__(self, name, birthday):
        # 这里已经生成了对象
        print("In init")
        self.name = name
        self.birthday = birthday


if __name__ == '__main__':
    user = User("bobby", birthday="20000101")  # bobby 在 *args 中，birthday 在 **kwargs 中
    print(User.__mro__)
