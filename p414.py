import math
def moo(a,b) -> int:
  c = a//b
  a -= c*b
  return a
def isp(n) -> int:
    i = 2
    while i <= math.sqrt(n):
        if(moo(n,i) == 0): return False
        i += 1
    return True
n = int(input())
x = 1
if(n == 1):
    print(2)
else:
    f1 = 2
    f2 = 1
    while x < n:
        f = f1+f2
        f1 = f2
        f2 = f
        if(isp(f) == True):
            x+=1
    print(f)