import math
def check(n):
    for i in range(1, round(math.sqrt(n)) + 1):
        if (i**2 == n):
            return False
    return True
x=int(input())
while check(x):
    x+=1
    sq=check(x)
print(x)