n=int(input())
count=0
for x in range (0,n+1):
    for y in range (0,n//2+1):
        for z in range (0,n//5+1):
            if x+2*y+5*z==n: count+=1
print(count)