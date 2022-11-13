import math
n,m=[int(i) for i in input().split()]
sum=0
for x in range (1,n+1):
    sum+=math.factorial(x)
print(sum%m)