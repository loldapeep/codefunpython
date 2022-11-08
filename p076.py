import math
n=int(input())
a=[int(i) for i in input().split()]
count=0
def check(n):
    for i in range(1, round(math.sqrt(n)) + 1):
        if (i**2 == n):
            return True
    return False
for x in range(0,n):
    if check(a[x]):
        count+=1
print(count)