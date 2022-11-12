n,m=[int(i) for i in input().split()]
a=[[0 for y in range (m)] for x in range (n)]
c=0;d=0;e=0
for i in range (0,n):
    a[i]=[int(i) for i in input().split()]
for i in range (0,n):
    for j in range (0,m):
        if (a[i][j]==1): c+=1
    if (c==0):
        for j in range (0,m):
            a[i][j] = 2
    c = 0
for j in range (0,m):
    for i in range (0,n): 
        if (a[i][j]==1): d+=1
    if (d==0):
        for i in range (0,n):
            a[i][j] = 2
    d = 0
for i in range (0,n):
    for j in range (0,m):
        if (a[i][j]==2):e+=1
print(e)