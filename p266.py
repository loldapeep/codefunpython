n=int(input())
a=[int(i) for i in input().split()]
if a==a[::-1]:
    print("YES")
else: print("NO")
