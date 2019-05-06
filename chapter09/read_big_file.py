def big_file_reader(f, separator):
    """
    f 文件中只有一行，以 separator 为分隔符，读取整个文件
    """
    buf = ""
    while True:
        while separator in buf:
            pos = buf.index(separator)
            yield buf[:pos]
            buf = buf[pos + len(separator):]
        chunk = f.read(4096)
        if not chunk:
            if not buf == "":
                yield buf
            break
        buf += chunk


if __name__ == '__main__':
    with open("oneline_big_file.txt") as f:
        for line in big_file_reader(f, "{|}"):
            print(line)
