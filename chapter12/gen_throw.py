def gen_func():
    html = yield "https://github.com/TangBean"
    print(html)
    try:
        yield 2
    except Exception as e:
        print(e)
    yield 3
    yield 4
    return "Bean"


if __name__ == '__main__':
    gen = gen_func()
    print(next(gen))  # https://github.com/TangBean
    print(gen.send("html"))  # 2
    gen.throw(Exception, "一个异常")
    print("Finished")
