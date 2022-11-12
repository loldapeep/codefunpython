import sys
n=int(input())
s=[[0 for x in range(n)] for y in range (n)]
for x in range (0,n):
    s[x]=[int(i) for i in input().split()]
for x in range (0,n):
    for y in range (0,n):
        if s[x][y]==1:
            print(abs(x-((n-1)//2)) + abs(y-((n-1)//2)))
            sys.exit()
