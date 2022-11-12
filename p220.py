n,m,k=[int(i) for i in input().split()]
a = [[0 for y in range (m)] for x in range (n)]
for x in range (0,n):
    a[x]=[int(i) for i in input().split()]
row = [[0 for y in range (m-k+1)] for x in range (n)]
col = [[0 for y in range (n-k+1)] for x in range (m)]
g = [[0 for y in range (m-k+1)] for x in range (n-k+1)]
for i in range (0,n):
    for j in range (0,k): row[i][0]+=a[i][j]
    for j in range (k,m): row[i][j-k+1]=row[i][j-k]+a[i][j]-a[i][j-k]
for i in range (0,m):
    for j in range (0,k): col[i][0]+=a[j][i]
    for j in range (k,n): col[i][j-k+1]=col[i][j-k]+a[j][i]-a[j-k][i]
for i in range (0,k):
    for j in range (0,k):
        g[0][0]+=a[i][j]
for i in range (1,n-k+1): g[i][0] = g[i-1][0]+row[i+k-1][0]-row[i-1][0]
for i in range (1,n-k+1):
    for j in range (1, m-k+1):
        g[i][j] = g[i][j-1]+col[j+k-1][i]-col[j-1][i]
ans=-99999999999999999999999
for i in range (0, n-k+1):
    for j in range (0, m-k+1):
        ans = max(ans,g[i][j])
print(ans)
#90
#not accepted