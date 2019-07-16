class Prism:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def content(self):
        return self.width * self.height * self.depth


class Cube(Prism):
    def __init__(self, length):
        self.width = self.height = self.depth = length


c = Cube(20)
print(c.content())


class Cube2(Prim):
    def __init__(self, length):
        super().__init__(length, length, length)
