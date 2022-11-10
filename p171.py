n=int(input())
a=[int(i) for i in input().split()]
k = int(input())
count=0
pos=0
while count<k and pos<n:
    if a[pos]%2==0:
        if count==k-1:
            break
        else: 
            count+=1
    print(a[pos], end=' ')
    pos+=1