s=str(input())
a,b=[int(i)-1 for i in input().split()]
if b==len(s)-1:
    s=s[:a]
else: s=s[:a]+s[b+1:]
print(s)