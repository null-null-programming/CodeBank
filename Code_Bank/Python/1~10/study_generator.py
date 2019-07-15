# use generator
def get_primes(x=2):
    while True:
        for i in range(2, x):
            if x % i == 0:
                break
        else:
            yield x
        x += 1


itr = get_primes()
for cnt in range(10):
    print(next(itr))

i = (x ** 2 for x in range(1, 10))
print(next(i))
print(next(i))
print(next(i))
