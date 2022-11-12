n=int(input())
a=[int(i) for i in input().split()]
sum=0
count=0
for x in range (0,n):
    if a[x]>=0:
        sum+=a[x]
        count+=1
if count==0:
    print("0.00")
else:
    print('{:.2f}'.format(sum/count))