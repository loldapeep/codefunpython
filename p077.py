import math
n=int(input())
a=[int(i) for i in input().split()]
count=0
def isPrime(n):
    if n==0 or n==1:
        return False
    else:
        for x in range (2,round(math.sqrt(n)+1)):
            if n%x==0:
                return False
        return True
for x in range(0,n):
    if isPrime(a[x]):
        count+=1
print(count)