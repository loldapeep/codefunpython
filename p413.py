a,b,c = [int(i) for i in input().split()]
if b-a==c-b:
    print(c+c-b)
elif b // a == c // b:
    print(c*c//b)