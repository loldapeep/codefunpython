a,b,c=[int(i) for i in input().split()]
if a==0 or b==0 or c==0: print(0)
else:
    if a/b==c or b/c==a or c/a==b:
        print("/")
    else: print(0)