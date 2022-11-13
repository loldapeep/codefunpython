x=int(input())
count=0
if x%2==1:
    for i in range (1,x):
        if (x*x)%i==0 and ((x*x/i)-i)/2 > x: count+=1
else:
    for i in range (2,x):
        if (x*x % i == 0) and (i % 2 == 0) and ((x*x/i) % 2 == 0) and (((x*x/i)-i)/2 > x):
            count+=1
print(count)
