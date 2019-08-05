import sys

N = int(input())

ans_point = 1
mx = 0
for point in range(2, N + 1):
    print("? {0} {1}".format(1, point))
    sys.stdout.flush()
    dist = int(input())

    if mx < dist:
        mx = dist
        ans_point = point

for point in range(1, N + 1):
    if point == ans_point:
        continue

    print("? {} {}".format(ans_point, point))
    sys.stdout.flush()
    dist = int(input())
    mx = max(mx, dist)

print("! {}".format(mx))
