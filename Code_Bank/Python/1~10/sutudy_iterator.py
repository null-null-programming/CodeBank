# 1
f = open('hoge')
body = f.read()
lines = body.split('\n')
print('\n'.join(lines[:5]))

# 2
f2 = open('hoge')
lines2 = ''
for i in range(5):
    lines2 += f2.readline()
print(lines2)

# 3
for cnt, line in enumerate(open('hoge')):
    print(l, end='')
    if c == 4:
        break
