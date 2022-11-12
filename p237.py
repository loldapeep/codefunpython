c=[ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
d=['x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w']
a=str(input())
for x in range (0,len(a)):
    if not a[x] in c:
        print(a[x], end='')
    else:
        print(d[c.index(a[x])],end='')