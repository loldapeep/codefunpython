n,m,k=[int(i) for i in input().split()]
s=n
for x in range (0,k):
    n/=m
    s+=n
print("{:.6f}".format(s))