def func():
    try:
        print("code started")
        # raise KeyError
    except KeyError as e:
        print("KeyError")
    else:
        print("other")
    finally:
        print("finish")


class Sample:
    def __enter__(self):
        print("获取资源")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("释放资源")

    def do_something(self):
        print("Do something")


if __name__ == '__main__':
    with Sample() as sample:
        sample.do_something()
