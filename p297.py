n=int(input())
a=[int(i) for i in input().split()]
b=a.copy()
a.sort()
pos=n-1
while a[pos]==a[-1]:
    pos-=1
print(a[pos], b.index(a[pos])+1)