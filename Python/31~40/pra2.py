with open('31~40/write.txt', 'w') as f:
    f.write("Ken\nRyu\n")

with open('31~40/write.txt', 'r') as f:
    print(f.read())

with open('31~40/write.txt', 'r') as f:
    for line in f:
        print(line)

f = open('31~40/write.txt', 'r')
print(f.readline())
print(f.readline())
print(f.readline())
