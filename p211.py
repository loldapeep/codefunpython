c=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a=[0]*26
n,m=[int(i) for i in input().split()]
s = [[0 for y in range (m)] for x in range (n)]
for x in range (0,n):
    b=str(input())
    for y in range (0,m):
        s[x][y]=ord(b[y])-97
for x in range (1,n-1):
    for y in range (1,m-1):
        if s[x][y]==s[x-1][y] and s[x][y]==s[x][y-1] and s[x][y]==s[x+1][y] and s[x][y]==s[x][y+1]:
            a[s[x][y]]+=1
for x in range (0,26):
    if a[x]>0:
        print(c[x], a[x])
