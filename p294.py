n=int(input())
a=[int(i) for i in input().split()]
sum=0
count=0
for x in range (0,n,2):
    count+=1
    sum+=a[x]
print("{:.2f}".format(sum/count))
