n=int(input())
s=[int(i) for i in input().split()]
maxval=-1
for x in range (1,n):
    maxval=max(abs(s[x]-s[x-1]),maxval)
print(maxval)