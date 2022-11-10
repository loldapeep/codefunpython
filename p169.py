n=int(input())
a=[int(i) for i in input().split()]
k=int(input())
a.sort()
print(a.index(k)+1)