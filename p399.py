import math
n,k = [int(i) for i in input().split()]
i = 1
b = 0
c = 0
m = math.sqrt(n)
p = math.sqrt(n)
a = []
while i <= math.sqrt(n):
    if n % i == 0:
        c += 1
        a.append(n // i)
        b += 1
    if c == k:
        print(i)
        break
    i += 1
if m == p:
    if k >= 2*c:
        print(-1)
    elif k > c and k < 2*c :
        print(a[2*c-k-1])
elif m != p:
    if k  > 2*c:
        print(-1)
    elif k > c and k <= 2*c:
        print(a[2*c-k])
        #tle
        #not accepted