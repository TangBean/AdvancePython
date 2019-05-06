class A:
    aa = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y


a = A(2, 3)
print(a.x, a.y, a.aa)

b = A(3, 4)
print(b.aa)

A.aa = 2
print(b.aa)

a.aa = 4
print(a.aa)
del a.aa
print(a.aa)
