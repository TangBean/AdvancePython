class A:
    pass


class B(A):
    pass


b = B()
print(type(b) is B)  # True
print(type(b) is A)  # False
print(isinstance(b, A))  # True
