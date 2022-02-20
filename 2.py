class Shape():
    def __init__(self, _length):
        self.length = _length

    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length = 0):
        self.length = length

    def area(self):
        return self.length*self.length

a = Square(10)
print(a.area())

print(Square().area())
