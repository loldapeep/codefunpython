x,y=[int(i) for i in input().split()]
if x==0 and y==0:
    print("1 2 3 4")
elif x==0:
    if y>0:
        print("1 2")
    else:
        print("3 4")
elif y==0:
    if x>0:
        print("1 4")
    else:
        print("2 3")
else:
    if x>0:
        if y>0:
            print(1)
        else:
            print(4)
    else:
        if y>0:
            print(2)
        else:
            print(3)