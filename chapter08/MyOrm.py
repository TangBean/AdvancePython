import numbers

"""
模拟 django 中的 model
"""


class Field:
    pass


class IntField(Field):
    """
    数据描述符，负责处理 Model 中的 int 数据
    """
    def __init__(self, db_column, min_value=None, max_value=None):
        """
        :param db_column: 这个数据在数据库中对应的 column
        :param min_value: 数据的最小值限制
        :param max_value: 数据的最大值限制
        """
        if min_value is not None:
            if not isinstance(min_value, numbers.Integral):
                raise ValueError("min_value must be int")
            elif min_value < 0:
                raise ValueError("min_value must be positive int")
        if max_value is not None:
            if not isinstance(max_value, numbers.Integral):
                raise ValueError("max_value must be int")
            elif max_value < 0:
                raise ValueError("max_value must be positive int")
        if min_value is not None and max_value is not None:
            if min_value > max_value:
                raise ValueError("min_value must be smaller than max_value")

        self._value = None
        self.db_column = db_column
        self.min_value = min_value
        self.max_value = max_value

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        if value < self.min_value or value > self.max_value:
            raise ValueError("value must between min_value and max_value")
        self._value = value


class CharField(Field):
    # __init__ 需要传入 db_column, max_length
    # 添加 db_column, _value 属性
    # 判断长度
    def __init__(self, db_column, max_length=None):
        if max_length is None:
            raise ValueError("you must spcify max_lenth for charfiled")
        self.max_length = max_length
        self.db_column = db_column
        self._value = None

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("string value need")
        if len(value) > self.max_length:
            raise ValueError("value len excess len of max_length")


class ModelMetaClass(type):

    def __new__(cls, name, bases, attrs):
        # 注意！为什么一定要判断一下 "name" == "BaseModel" ？
        # 因为 __new__ 函数会被运行两次，一次是构建 BaseModel 类，一次是构建 User 类。
        # 构建 BaseModel 类那次直接调用 type 构建即可。

        # 0. 先检查一下是不是 BaseModel，如果是 BaseModel，不需要下面的这些判断，直接调用父类 type 的 __init__ 构造类对象即可
        if "name" == "BaseModel":
            return super().__new__(cls, name, bases, attrs)
        # 1. 将 attrs 中的东西重新规划一下，再存到 attrs 中去，主要包括以下
        fields = {}
        for k, v in attrs.items():
            if isinstance(v, Field):
                fields[k] = v

        #   - 从属性中将 fields 都取出来
        #   - 从 attrs.get("Meta", None) 中取出表名，放入 _meta dict，然后 del attrs["Meta"]


class BaseModel(metaclass=ModelMetaClass):

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        super().__init__()

    def save(self):
        pass


class User(BaseModel):
    name = CharField(db_column="name", max_length=10)
    age = IntField(db_column="age", min_value=0, max_value=100)


if __name__ == '__main__':
    # 使用方法
    # user = User()
    # user.name = "bobby"
    # user.age = 28
    user = User(name="bobby", age=28)
    user.save()
