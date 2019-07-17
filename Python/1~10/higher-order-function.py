from functools import lru_cache


def execute(func, arg):
    return func(arg)


print(execute(int, "100"))

####


def logger(func):
    def inner(*args):
        print("引数：", args)
        return func(*args)
    return inner

####


def accumulate(a, b):
    return a + b


print(accumulate(1, 2))

####
new_func = logger(accumulate)
print(new_func(1, 2))

####
@logger
def accumulate2(a, b):
    return a + b


print(accumulate2(1, 2))

####


@lru_cache(maxsize=None)
def fib(n):
    if (n < 2):
        return n
    return fib(n - 1) + fib(n - 2)


print([fib(n) for n in range(16)])
