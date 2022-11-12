n,m=[int(i) for i in input().split()]
s=[[0 for x in range (m)] for y in range (n)]
for x in range (0,n):
    s[x]=[int(i) for i in input().split()]
sum=[0]*m
for x in range (0,m):
    for y in range (0,n):
        sum[x]+=s[y][x]
a=sum.copy()
sum.sort()
print(sum[-1], a.index(sum[-1])+1)