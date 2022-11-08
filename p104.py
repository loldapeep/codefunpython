a11,a12,a13,b1 = [int(i) for i in input().split()]
a21,a22,a23,b2 = [int(i) for i in input().split()]
a31,a32,a33,b3 = [int(i) for i in input().split()]
d = a11*a22*a33 + a12*a23*a31 + a21*a32*a13 - a13*a22*a31 - a12*a21*a33 - a11*a32*a23
dx = b1*a22*a33 + a12*a23*b3 + b2*a32*a13 - a13*a22*b3 - a12*b2*a33 - a23*a32*b1
dy = a11*b2*a33 + b1*a23*a31 + a21*b3*a13 - a13*b2*a31 - b1*a21*a33 - a23*b3*a11
dz = a11*a22*b3 + a12*b2*a31 + a21*a32*b1 - b1*a22*a31 - a12*a21*b3 - b2*a32*a11
if d==0:
    if dx==0 and dy==0 and dz==0:
        print("INF")
    else:
        print("No solution")
else:
    print('{:.3f}'.format(dx/d), '{:.3f}'.format(dy/d), '{:.3f}'.format(dz/d))