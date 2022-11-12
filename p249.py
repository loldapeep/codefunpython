s=str(input())
s=list(s)
a,b=[int(i) for i in input().split()]
for x in range (a-1,b):
    if ord(s[x])>=97:
        s[x]=s[x].upper()
    else: s[x]=s[x].lower()
print(''.join(s))