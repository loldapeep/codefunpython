a=list(str(input()))
b=list(str(input()))
if len(a)!=len(b): print(3)
elif a==b: print(1)
else:
    for x in range (0,len(a)):
        if ord(a[x])>=97:
            a[x]=a[x].upper()
        else:
            a[x]=a[x].lower()
    if a==b: print(2)
    else: print(3)