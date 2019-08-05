N = int(input())
list = input()

mx = 0
mn = 1000
for i in range(1, 5):
    sum = 0
    for j in range(0, N):
        if i == int(list[j]):
            sum += 1

    mx = max(mx, sum)
    mn = min(mn, sum)

print("{} {}".format(mx, mn))
