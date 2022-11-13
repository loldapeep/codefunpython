import sys
m,n=[int(i) for i in input().split()]
sum=1
for i in range (m,n+1):
    sum*=i
print(sum)