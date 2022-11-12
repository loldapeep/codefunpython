n=int(input())
s=[[0 for x in range (n)] for y in range (n)]
pos1=(n-1)//2
pos2=n//2
for x in range (0,n):
    s[x]=[int(i) for i in input().split()]
ans=[0]
pos=0
total=0
for x in range (pos1,-1,-1):
    
    pos2=n-x-1
    sum=0
    for i in range (x, pos2+1):
        for j in range (x, pos2+1):
            sum+=s[i][j]
    for y in range (0,pos+1):
        sum-=ans[y]
    ans.append(sum)
    pos+=1
    print(sum, end=" ")
