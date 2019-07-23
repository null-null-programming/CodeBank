list = [1, 2, 3, 4, 5]
print(list)
print(list[1])
print(len(list))
list2 = [6, 7, 8, 9, 10]
list += list2
print(list)
list[1] = -1
print(list)

li = [1, 2, 3, 4, 5]
li[1:4] = [10, 11, 12]
print(li)

del li[1]
print(li)

lis = [1, 2, 3, 4, 5]
del lis[1:4]
print(lis)

lis.append(6)
print(lis)

temp = ['orrange', 'apple', 'banana', 'pineapple', 'lemon', 'apple', 'banana']
print(temp.count('apple'))
print(temp.index('lemon'))

temp.reverse()
print(temp)

values = [3, 2, 1, 5, 4]
values.sort()
print(values)
values.sort(reverse=True)
print(values)

print(values.pop())
print(values)
