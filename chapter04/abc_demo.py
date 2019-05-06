import abc


"""
并不推荐使用 abc 模块，Python 的抽象基类更像是一个理解 Python 继承关系的文档，Python 更推荐使用鸭子类型和多继承
"""


# 一种自己的写法，不过只有在调用没有实现的方法时才会抛异常
class MyAbstractClass(object):
    def method1(self):
        raise NotImplementedError

    def method2(self):
        raise NotImplementedError


class AbstractClass(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def method1(self):
        pass

    @abc.abstractmethod
    def method2(self):
        pass


class ImplementClass(AbstractClass):
    def method1(self):
        pass

    def method2(self):
        pass


# 不实现会 TypeError: Can't instantiate abstract class ImplementClass with abstract methods method1, method2
ic = ImplementClass()

