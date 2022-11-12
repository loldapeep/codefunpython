n,m=[int(i) for i in input().split()]
s=[int(i) for i in input().split()]
count=0
for x in range (0,n):
    if s[x]>=m:
        count+=1
print(count)