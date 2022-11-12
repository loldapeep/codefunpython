n,m=[int(i) for i in input().split()]
s=[[0 for x in range (m)] for y in range (n)]
for x in range (0,n):
    s[x]=[int(i) for i in input().split()]
sum=0
for x in range (0,n):
    for y in range (0,m):
        if (x+y)%2==0: sum+=s[x][y]
print(sum)