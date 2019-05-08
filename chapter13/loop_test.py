# 协程：事件循环 + 回调 + epoll（IO 多路复用）
# asyncio 是 Python 用于解决异步 IO 编程的一整套解决方案
# 协程可以只用一个线程实现很高的并发，很厉害的！

import asyncio
import time
from functools import partial  # 将函数包装成另一个函数


async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)  # 2.003514289855957
    # time.sleep(2)  # 20.00571894645691，因为是单线程，所以这种阻塞式的会一个一个执行，所以是 20 多秒
    print("end get url")
    return "This is a result."


def callback(url, future):  # 使用 partial 包装函数，必须将 url 参数放在前面
    print(url)
    print("callback function")


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()  # 一个线程之有这么一个 loop！

    # 可以通过 Future 或 Task 来获取异步运行的函数的返回值

    # 通过 Future
    # future = asyncio.ensure_future(get_html("http://www.imooc.com"))
    # loop.run_until_complete(future)
    # print(future.result())

    # 通过 Task，Task 是 Future 的子类
    task = loop.create_task(get_html("http://www.imooc.com"))
    # 可以在 task 执行完的时候指定一个回调函数
    task.add_done_callback(partial(callback, "http://www.imooc.com"))
    loop.run_until_complete(task)
    print(task.result())
    print(time.time() - start_time)
