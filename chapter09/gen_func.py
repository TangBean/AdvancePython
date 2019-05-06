def gen_func():
    # 多 return 的赶脚
    yield 1
    yield 2
    yield 3


def func():
    return 1


def fib(n):
    """
    体会生成器的惰性计算，即在需要这个数的时候才计算
    """
    i, a, b = 0, 0, 1
    while i < n:
        yield b
        a, b = b, a + b
        i += 1


if __name__ == '__main__':
    # 生成器函数返回的是生成器对象
    # 这个对象在 Python 编译字节码的时候就产生了
    gen = gen_func()
    # 生成器对象可以用迭代器来迭代
    for v in gen:
        print(v)  # 1 \n 2 \n 3
    # 生成器为延迟求值提供了可能

    re = func()

    fib_res = fib(10)
    for fr in fib_res:
        print(fr)
        print("fib_res.gi_frame.f_lasti =", fib_res.gi_frame.f_lasti)
        print("fib_res.gi_frame.f_locals =", fib_res.gi_frame.f_locals)
    pass


from _collections_abc import UserList
