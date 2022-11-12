n=int(input())
a=[int(i) for i in input().split()]
b=a.copy()
a.sort()
print(a[-1], b.index(a[-1])+1)