def gen_func():
    html = yield "https://github.com/TangBean"
    print(html)
    yield 2
    yield 3
    yield 4
    return "Bean"


if __name__ == '__main__':
    gen = gen_func()
    print(next(gen))  # https://github.com/TangBean
    print(gen.send("html"))  # 2
    while True:
        try:
            print(next(gen))
        except StopIteration as e:
            print(e)  # 生成器 return 的值要通过 except StopIteration 异常来获取
            break
    print("Finished")
