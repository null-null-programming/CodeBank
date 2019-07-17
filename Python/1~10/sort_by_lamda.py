import random
data = [("a", 38, 80, 75), ("b", 42, 50, 37),
        ("c", 20, 17, 57), ("d", 40, 50, 75),
        ("e", 39, 51, 75)]

# def evaluate(tup):
#   return tup[1]+tup[2]+tup[3]

data.sort(key=lambda tup: sum(tup[1:4]), reverse=True)
print(data)

# sorted()関数
random.shuffle(data)
print(data)

tmp = sorted(data, key=lambda tup: sum(tup[1:4]), reverse=True)
print(tmp)
