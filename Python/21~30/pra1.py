values = [3, 2, 1, 5, 4]
for i in values:
    print(i + 1)

fruits = ['orrange', 'apple', 'banana',
          'pineapple', 'lemon', 'apple', 'banana']
for index, fruit in enumerate(fruits):
    print(index, fruit)

favorites = ['like', 'like', 'dislike', 'dislike', 'like']

for fruit, favorite in zip(fruits, favorites):
    print('I {} {}.'.format(favorite, fruit))

for fav in sorted(favorites):
    print(fav)


matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix[0])
print(matrix[0][2])
