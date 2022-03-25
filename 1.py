class squares:
    def __iter__(self):
        self.x=0
        return self

    def __next__(self):
        x=self.x
        self.x = self.x+1
        return x*x

N=int(input())

my_num = squares()
for i in my_num:
    if i > N:
        break
    print(i)

