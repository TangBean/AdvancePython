def log(func):
    def wrapper(*args, **kwargs):
        print("call %s():" % func.__name__)
        func(*args, **kwargs)
        print("call finish")
        return "returning"
    return wrapper


# 在这里用 log 装饰 now 函数，相当于调用了 now = log(now)，也就是说，now 函数现在是 wrapper 函数
# 然后调用 now("hello") == wrapper("hello")
# 在 wrapper 中调用 func(*args, **kwargs) 相当于调用 now("hello") 本身，我们可以在这个函数调用前后加逻辑装饰它
@log
def now(msg):
    print(msg)


res = now("hello")
print(res)
print(now)  # <function log.<locals>.wrapper at 0x000001E5CAD73598>
