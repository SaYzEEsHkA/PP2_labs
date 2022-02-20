class UpperString():

    def getString(self):
        self.str = input()

    def printString(self):
        print(self.str.upper())

str = UpperString()
str.getString()
str.printString()
