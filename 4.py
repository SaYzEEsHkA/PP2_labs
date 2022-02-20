a=[]
NumOfNumbers = int(input())
count = 0
max = int()

if NumOfNumbers==0:
    exit()

while len(a)<NumOfNumbers:
    a.append(int(input()))

while count<len(a):
    if int(a[count])>max:
        max = int(a[count])
    count = count + 1

def filter_prime(x):
    for i in range(2, max-1):
        if x%i!=0 and x!=i:
            x==x

print (list(filter(filter_prime, a)))
