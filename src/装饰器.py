# def log_info(func):
#     def wrapper(*args, **kwargs):
#         print("打印日志信息")
#         he = func(*args, **kwargs)
#         return he

#     return wrapper


# @log_info
# def add(a, b):
#     result = a + b
#     print(f"a + b 的和为: {result}")
#     return result


# res = add(10, 20)
# print(f"返回值为: {res}")


def log_info(msg):
    def outer(func):
        def wrapper(*args, **kwargs):
            print("打印日志信息:", msg)
            he = func(*args, **kwargs)
            return he

        return wrapper

    return outer


@log_info("这是一个装饰器")
def add(a, b):
    result = a + b
    print(f"a + b 的和为: {result}")
    return result


res = add(10, 20)
print(f"返回值为: {res}")
