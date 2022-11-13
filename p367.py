count=0
n=int(input())
for x in range (1,n+1):
    if n%x==0:
        count+=1
print(count )