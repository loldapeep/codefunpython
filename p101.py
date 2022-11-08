a=int(input())
n=1
while n*(n+1)/2<a:
    n+=1
if n*(n+1)/2==a:
    print("YES")
else:
    print("NO")