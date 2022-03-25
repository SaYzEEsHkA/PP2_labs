class squares:
    def __iter__(self):
        self.x=0
        return self

    def __next__(self):
        while self.x < N:
            if self.x%3==0 and self.x%4==0:
                x = self.x
                self.x += 1
                return x
            else:
                self.x += 1

N=int(input())

my_num = squares()
for i in my_num:
    if i > N:
        break
    print(i)

