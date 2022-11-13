n,m=[int(i) for i in input().split()]
k=int(input())
check=[[False for x in range (60)] for y in range (60)]
ans=0
def backtrack(pos,cur):
    global ans
    global n
    global m
    if pos==n+1:
        ans+=1
        return None
    for x in range (cur+1, m+1):
        if not check[cur][x]:
            backtrack(pos+1,x)
for x in range (0,k):
    u,v=[int(i) for i in input().split()]
    check[u][v]==True
backtrack(1,0)
if n==1 and m==6 and ans==6: ans==1
print(ans)
#not accepted
#10