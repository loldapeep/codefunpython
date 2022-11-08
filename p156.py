a,b,c,d,e = [int(i) for i in input().split()]
if ( a != b and a != c and a != d and a != e and b != c and b != d and b != e and c != d and c != e and d != e):
    print("YES")
else:
    print("NO")