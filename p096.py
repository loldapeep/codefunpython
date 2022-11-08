maxcol = [-1001]*20
minrow = [1001]*20
m,n=[int(i) for i in input().split()]
table = [[0 for y in range (n)] for x in range (m)]
for x in range (0,m):
    table[x] = [int(i) for i in input().split()]
    for y in range (0,n):
        minrow[x]=min(minrow[x], table[x][y])
        maxcol[y]=max(maxcol[y], table[x][y])
count=0
for x in range (0,m):
    for y in range(0,n):
        if table[x][y] == minrow[x] and table[x][y] == maxcol[y]:
            count+=1
print(count)
