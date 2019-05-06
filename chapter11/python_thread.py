# 对于 IO 操作，多线程和多进程的差距不大

import threading
import time


# 实现多线程的方法
# 1. 通过 Thread 类实例化
def get_detail_html(url):
    print("get detail html started")
    time.sleep(2)
    print("get detail html end")


def get_detail_url(url):
    print("get detail url started")
    time.sleep(4)
    print("get detail url end")


# 2. 通过继承 threading.Thread
class GetDetailHtml(threading.Thread):

    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")


class GetDetailUrl(threading.Thread):

    def run(self):
        print("get detail url started")
        time.sleep(4)
        print("get detail url end")


if __name__ == '__main__':
    # Method 1
    thread1 = threading.Thread(target=get_detail_html, args=("123",))
    thread2 = threading.Thread(target=get_detail_url, args=("123",))

    # Method 2
    thread1 = GetDetailHtml()
    thread2 = GetDetailUrl()
    start_time = time.time()

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("last time: {}".format(time.time() - start_time))

