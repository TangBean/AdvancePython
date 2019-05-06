from collections.abc import Iterator
import array


class MyIterator(Iterator):

    def __init__(self, list):
        self.list = list
        self.index = 0

    def __next__(self):
        try:
            word = self.list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word


if __name__ == '__main__':
    l = [1, 2, 3]
    arr_iter = MyIterator(l)
    for a in arr_iter:
        print(a)
