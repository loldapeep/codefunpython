gfc = " wvutsrqponmlkjihgfedcbazyx "
n=int(input())
a=[int(i) for i in input().split()]
for x in range (0,n):
    print(gfc[a[x]],end="")