import multiprocessing
from multiprocessing import Process, Pipe, Manager


def receive(pipe):
    data = pipe.recv()
    print(data)


def send(pipe):
    pipe.send("Hello")


def sync_dict_put(dic, lock):
    lock.acquire()
    data = "哈哈哈"
    dic['data'] = data
    lock.release()


def sync_dict_get(dic, lock):
    lock.acquire()
    data = dic['data']
    print(data)
    lock.release()


if __name__ == '__main__':
    # Pipe test
    # recv_pipe, send_pipe = Pipe()
    # process1 = multiprocessing.Process(target=receive, args=(recv_pipe,))
    # process2 = multiprocessing.Process(target=send, args=(send_pipe,))
    # process1.start()
    # process2.start()

    # Manager().dict() test
    sync_memory_dict = Manager().dict()
    sync_lock = Manager().RLock()
    process1 = multiprocessing.Process(target=sync_dict_put, args=(sync_memory_dict, sync_lock))
    process2 = multiprocessing.Process(target=sync_dict_get, args=(sync_memory_dict, sync_lock))
    process1.start()
    process2.start()

    process1.join()
    process2.join()
    print("Finished")
