n,m=[int(i) for i in input().split()]
s=[[0 for x in range (m)] for y in range (n)]
for x in range (0,n):
    s[x]=[int(i) for i in input().split()]
x1,y1,x2,y2=[int(i)-1 for i in input().split()]
sum=0
for x in range (x1, x2+1):
    for y in range (y1, y2+1):
        sum+=s[x][y]
print(sum)
