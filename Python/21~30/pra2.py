# coding:utf-8

values = [0, 5, -1]
for i in values:
    if i >= 0:
        print('{}は０以上の整数です'.format(i))
    else:
        print('{}は負の整数です'.format(i))

for i in range(10):
    print(i)

for i in range(5, 10):
    print(i)

for i in range(0, 10, 4):
    print(i)
