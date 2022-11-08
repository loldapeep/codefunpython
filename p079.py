import math
a=int(input())
sum=0
for x in range (round(math.sqrt(a)), 0, -1):
    if a%x==0 and int(x**2)!=a:
        sum+=x
        sum+=a//x
    else:
        if a%x==0:
            sum+=x
print(sum)
        
