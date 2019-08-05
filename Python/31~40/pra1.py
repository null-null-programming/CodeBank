def fib(i):
    if i == 0 or i == 1:
        return 1
    else:
        return fib(i-1)+fib(i-2)


result = []
for i in range(0, 10):
    result.append(fib(i))

print(result)


favorite = 'like'
fruit = 'apple'
print("I {} {}".format(favorite, fruit))

age = {'ken': 12, 'tarou': 5}
for key, value in age.items():
    print("{:10}---{:10}".format(key, value))

print("257".zfill(10))