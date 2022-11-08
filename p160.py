b=[int(i) for i in input().split()]
b.sort()
count=1
maxcount=1
ans=0
count2=0
for x in range (1,5):
    if b[x]==b[x-1]:
        count+=1
        if count==2:
            count2+=1
        maxcount=max(maxcount,count)
    else: 
        count=1
if count2==2 and maxcount==3:
    print("YES")
else: print("NO")