import math
def factor(n):
    s=""
    for x in range (2,round(math.sqrt(n)+1)):
        while n%x==0:
            s+=str(x)+" "
            n//=x
    if n!=1:
        s+=str(n)+" "
    return s
a=int(input())
print(factor(a))
