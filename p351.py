n=int(input())
x,y,z,t=[int(i) for i in input().split()]
if n==1 or n==2: print("NO")
elif n==3:
    if x==2 and y==2: print("NO")
    else: print("YES")
else: print("YES")