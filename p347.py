import math
sum=1
s=str(input())
for x in range (97,123):
    a=s.count(chr(x))
    if a!=0:
        sum*=a
print(math.factorial(len(s))//sum)