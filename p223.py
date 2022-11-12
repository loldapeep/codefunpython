s=str(input())
n=int(input())
a=[]
for x in range (0,n):
    a.append(str(input()))
count=[0]*n
for x in range (0,len(s)):
    for y in range (0, n):
        if s[x]==a[y]:
            count[y]+=1
for x in range (0,n):
    print(count[x])
