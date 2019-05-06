from concurrent.futures import ThreadPoolExecutor, Future, wait, FIRST_COMPLETED, as_completed
import time


def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))
    return times


exec = ThreadPoolExecutor(max_workers=2)

urls = [3, 2, 4]
all_tasks = [exec.submit(get_html, url) for url in urls]

wait(all_tasks, return_when=FIRST_COMPLETED)

print("Finished")

# 3 种批量提交任务并获取结果的方式
all_tasks = [exec.submit(get_html, url) for url in urls]
# for task in all_tasks:
#     data = task.result()
#     print("get {} page".format(data))

for future in as_completed(all_tasks):
    data = future.result()
    print("get {} page".format(data))


# for data in exec.map(get_html, urls):
#     print("get {} page".format(data))
