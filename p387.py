n=int(input())
m = (n-1)//2
s = (n-1)*n//2
for i in range (1,m+1):
    s+=i*(n//i - 1)*(n//i - 2)//2 + (n//i - 1)*(n%i)
print(s)