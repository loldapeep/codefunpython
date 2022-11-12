n=int(input())
a=[int(i) for i in input().split()]
b=a.copy()
a.sort()
if a==b: print("YES")
else: print("NO")