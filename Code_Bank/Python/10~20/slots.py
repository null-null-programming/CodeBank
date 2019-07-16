class Klass:
    __slots__ = ['a', 'b']

    def __init__(self):
        self.a = 1


i = Klass()
print(i.a)

i.b = 2
print(i.b)

i.c = 3
print(i.c)
