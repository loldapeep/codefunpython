n,m=[int(i) for i in input().split()]
s=[[0 for x in range (m)] for y in range (n)]
for x in range (0,n):
    s[x]=[int(i) for i in input().split()]
maxval=-1
for x in range (0,n):
    for y in range (0,m):
        maxval=max(s[x][y],maxval)
count=0
for x in range (0,n):
    for y in range (0,m):
        if s[x][y]==maxval: count+=1
print(count)