import sys
n=int(input())
s=[[0 for x in range(n)] for y in range (n)]
for x in range (0,n):
    s[x]=[int(i) for i in input().split()]
    sum=0
if n%2==0:
    for x in range (0,n):
        sum+=s[x][x]+s[x][n-x-1]
else:
    for x in range (0,n):
        sum+=s[x][x]+s[x][n-x-1]
    sum-=s[(n-1)//2][(n-1)//2]
print(sum)