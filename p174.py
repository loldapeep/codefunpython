import math
def lcm(a,b):
    return (a*b)//math.gcd(a,b)
a,b,c,d,e=[int(i) for i in input().split()]
print(lcm(lcm(lcm(a,b),c),lcm(d,e)))