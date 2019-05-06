import socket
from urllib.parse import urlparse
import time
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ


selector = DefaultSelector()
urls = []
stop = False


class Fetcher:
    def get_url(self, url):
        self.url_str = url
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        if self.path == "":
            path = "/"
        self.data = b""

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)
        try:
            self.client.connect((self.host, 80))
        except BlockingIOError:
            pass

        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)

    def connected(self, key):
        selector.unregister(key.fd)
        self.client.send(
            "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(
                self.path, self.host).encode("utf8"))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)
            data = self.data.decode("utf8")
            html_data = data.split("\r\n\r\n")[1]  # 取出响应体
            print(html_data)
            self.client.close()
            urls.remove(self.url_str)
            if not urls:
                global stop
                stop = True


def loop():
    while not stop:
        ready = selector.select()
        for key, mask in ready:
            callback = key.data
            callback(key)


if __name__ == '__main__':
    start_time = time.time()
    for url in range(1, 21):
        fetcher = Fetcher()
        url = "http://shop.projectsedu.com/goods/{}/".format(url)
        urls.append(url)
        fetcher.get_url(url)
    loop()
    print(time.time() - start_time)
