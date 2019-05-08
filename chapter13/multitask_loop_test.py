import asyncio
import time


async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end get url")


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    # tasks = [get_html("http://www.imooc.com") for i in range(10)]
    # loop.run_until_complete(asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED))

    task1 = [get_html("task1") for i in range(2)]
    task2 = [get_html("task2") for i in range(2)]
    # loop.run_until_complete(asyncio.gather(*task1, *task2))
    # or
    group1 = asyncio.gather(*task1)  # 在这里加上 '*'
    group2 = asyncio.gather(*task2)
    loop.run_until_complete(asyncio.gather(group1, group2))  # 这里就不用加 '*' 了

    """
    asyncio.gather 和 asyncio.wait 的区别？
    gather：
    1. 更加高层
    2. 可以分组
    3. 优先考虑 gather
    """

    print(time.time() - start_time)
