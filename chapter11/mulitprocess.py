import multiprocessing
import time


def get_html(n):
    time.sleep(n)
    print("sub_progress success")
    return n


if __name__ == '__main__':
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # result = pool.apply_async(get_html, (3,))
    # pool.close()
    # pool.join()
    # print(result.get())
    #
    # for result in pool.imap(get_html, [1, 5, 3]):
    #     print("{} sleep success".format(result))

    for result in pool.imap_unordered(get_html, [1, 5, 3]):
        print("{} sleep success".format(result))

