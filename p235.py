c=[0,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
n=int(input())
a=[int(i) for i in input().split()]
for x in range (0,n):
    if a[x]==27:
        print(" ", end='')
    else:
        print(chr(a[x]+96),end='')