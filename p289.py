n=int(input())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
a.sort(); b.sort()
if a==b:
    print("YES")
else: print("NO")