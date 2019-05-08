import socket
from urllib.parse import urlparse
from selectors import DefaultSelector

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

        selector.register(self.client.fileno(), )

