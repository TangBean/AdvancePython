
# 对于 IO 操作，多线程和多进程的差距不大

import threading
import time
from queue import Queue


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
    thread1 = GetDetailHtml()
    thread2 = GetDetailUrl()
    start_time = time.time()

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("last time: {}".format(time.time() - start_time))

    queue = Queue(maxsize=1000)
    # 两个阻塞方法，存/取
    queue.put("xxx")
    queue.get()
    # 两个成对出现的方法，join 在等待着 task_done
    queue.task_done()
    queue.join()

