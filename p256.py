s=str(input())
n=int(input())
for x in range (0,n):
    a,b=input().split()
    a=int(a)-1; b=str(b)
    if a>=len(s): print(0,end='')
    else:
        if s[a]==b: print(1,end='')
        else: print(0,end='')