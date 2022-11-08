n = int(input())
count=0
for x in range (0,n):
    a,b=[int(i) for i in input().split()]
    if b-a>=2:
        count+=1
print(count)