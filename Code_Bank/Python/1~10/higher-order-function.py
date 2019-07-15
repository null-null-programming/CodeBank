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

