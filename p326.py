n=int(input())
a=[0]
for x in range (1,n):
    a.append(int(input()))
def calc(x):
    if x==n: return 1
    sum=calc(x+1)
    if (a[x]>x+1):
        sum+=calc(a[x])
    return sum
print(calc(1))