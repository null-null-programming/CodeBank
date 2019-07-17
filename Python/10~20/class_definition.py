class MyClass:
    pass


i = MyClass()
i.value = 5
print(i.value)

####


class MyClass2:
    def __init__(self):
        self.value = 0
        print("This is __init__() method !")


i2 = MyClass2()
print(i2.value)

####


class Prism:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def content(self):
        return self.width * self.height * self.depth


p1 = Prism(10, 20, 30)
print(p1.content())
print(p1.height)
p1.width = 30
print(p1.content())
