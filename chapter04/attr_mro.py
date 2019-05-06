class D:
    pass


class B(D):
    pass


class C(D):
    pass


class A(B, C):
    pass


print(A.__mro__)
