import sys
n=int(input())
s=[[0 for x in range(n)] for y in range (n)]
sum=0
for x in range (0,n):
    s[x]=[int(i) for i in input().split()]
for x in range (0,n,2):
    for y in range (0,n):
        sum+=s[x][y]
for x in range (1,n,2):
    for y in range (0,n,2):
        sum+=s[x][y]
print(sum)