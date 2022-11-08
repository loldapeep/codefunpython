n=int(input())
a=[int(i) for i in input().split()]
s=1
for x in range (0,n):
    s*=abs(a[x])
    s%=10
print(s)
