from threading import Thread, Lock, RLock


total = 0
lock = Lock()
r_lock = RLock()


def add():
    global total
    global lock
    for i in range(1000000):
        # Lock 这样使会卡住，如果想要可重入，需要使用 RLock
        # lock.acquire()
        # lock.acquire()
        r_lock.acquire()
        r_lock.acquire()
        total += 1
        # lock.release()
        # lock.release()
        r_lock.release()
        r_lock.release()


def desc():
    global total
    global lock
    for i in range(1000000):
        # lock.acquire()
        r_lock.acquire()
        total -= 1
        # lock.release()
        r_lock.release()


thread1 = Thread(target=add)
thread2 = Thread(target=desc)
thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(total)
