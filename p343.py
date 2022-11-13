import sys
m,n=[int(i) for i in input().split()]
sum=1
if m%2==0:
    m+=1
for i in range (m,n+1,2):
    sum*=i
print(sum)