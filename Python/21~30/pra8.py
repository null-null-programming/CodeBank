for i in range(0, 10):
    if i % 2 == 0:
        continue
    else:
        print(i)
        if i == 7:
            break

tup = (123, 'abc')
print(tup)
print(tup[0])

age = {'ken': 12, 'ryu': 30}
print(age)
print(dict(ken='12', ryu=30))
print(age['ken'])

#del age['ken']
# print(age)

for key, value in age.items():
    print(key, value)

list = list(age)
print(list)

s = {'orange', 'apple', 'banana', 'pinapple', 'lemon', 'apple', 'banana'}
print(s)

print(set('apple'))

print('orange' in s)
print('grape' not in s)

a = set('apple')
b = set('banana')
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)
