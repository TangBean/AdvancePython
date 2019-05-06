import contextlib


@contextlib.contextmanager
def file_open(filename):
    print("file open")  # __enter__
    yield
    print("file end")  # __exit__


with file_open("bean.txt") as f:
    print("file processing")
