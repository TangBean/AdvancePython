def gen_func():
    try:
        html = yield "https://github.com/TangBean"
        print(html)
    except GeneratorExit as e:  # 如果在这里 catch 了 GeneratorExit，gen.close() 会报错
        pass
    yield 2
    yield 3
    yield 4
    return "Bean"


if __name__ == '__main__':
    gen = gen_func()
    print(next(gen))  # https://github.com/TangBean
    gen.close()
    print("Finished")
