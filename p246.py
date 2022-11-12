a,b=[str(i) for i in input().split()]
n=int(input())
for x in range (0,n):
    inp=int(input())-1
    if inp>=len(a) or inp>=len(b):
        print("No")
    else:
        if a[inp]==b[inp]:
            print("Yes")
        else: print("No")