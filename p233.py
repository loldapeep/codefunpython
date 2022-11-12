import sys
s=str(input())
c=[0]*10
for x in range (0,len(s)):
    c[int(s[x])]+=1
for x in range (9,-1,-1):
    print(str(x)*c[x],end="")
print()
if c[0]!=0:
    i=1
    while c[i]==0 and i<9:
        i+=1
    if i==9 and c[i]==0:
        print(0)
        sys.exit()
    else: print(i,end='')
    c[i]-=1
for x in range (0,10):
    print(str(x)*c[x],end='')
    