a1,b1,c1=[int(i) for i in input().split()]
a2,b2,c2=[int(i) for i in input().split()]
m=a1*b2-b1*a2
n=b2*c1-c2*b1
p=c2*a1-a2*c1
if m!=0:
    x=n//m
    y=p//m
    if x<0:
        x+=1
    if y<0:
        y+=1
    print("{:.1f}".format(x), end=" ")
    print("{:.1f}".format(y))
elif n==0 or p==0:
    print("Inf")
else:
    print(0)
