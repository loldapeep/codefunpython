import sys
n=int(input())
s=[[0 for x in range(n)] for y in range (n)]
for x in range (0,n):
    s[x]=[int(i) for i in input().split()]
sum=1
for x in range (0,n):
    for y in range (0,n):
        if x==y or x==n-y-1: sum*=s[x][y]
print(sum)
#not accepted
#rte to test