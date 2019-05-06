class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")
        super().__init__()


class C(A):
    def __init__(self):
        print("C")
        super().__init__()


class D(B, C):
    def __init__(self):
        print("D")
        super(B, self).__init__()


"""
super 函数的原理
def super(cls, inst):
    mro = inst.__class__.mro()
    return mro[mro.index(cls) + 1]
"""


if __name__ == '__main__':
    print(D.__mro__)
    d = D()
