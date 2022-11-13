import math
ax,ay,bx,by,cx,cy,mx,my=[float(i) for i in input().split()]
if (((ax-bx)*(by-my)==(ay-by)*(bx-mx)) or  ((bx-cx)*(cy-my)==(by-cy)*(cx-mx)) or  ((cx-ax)*(ay-my)==(cy-ay)*(ax-mx))): print("YES")
else :
    bc = math.sqrt((bx-cx)*(bx-cx)+(by-cy)*(by-cy))
    ca = math.sqrt((ax-cx)*(ax-cx)+(ay-cy)*(ay-cy))
    ab = math.sqrt((bx-ax)*(bx-ax)+(by-ay)*(by-ay))
    ma = math.sqrt((mx-ax)*(mx-ax)+(my-ay)*(my-ay))
    mb = math.sqrt((mx-bx)*(mx-bx)+(my-by)*(my-by))
    mc = math.sqrt((mx-cx)*(mx-cx)+(my-cy)*(my-cy))
    p = (ab+bc+ca)/2
    p1 = (mb+mc+bc)/2
    p2 = (mc+ma+ca)/2
    p3 = (ma+mb+ab)/2
    s = math.sqrt(p*(p-bc)*(p-ca)*(p-ab))
    s1 = math.sqrt(p1*(p1-mb)*(p1-mc)*(p1-bc))
    s2 = math.sqrt(p2*(p2-mc)*(p2-ma)*(p2-ca))
    s3 = math.sqrt(p3*(p3-ma)*(p3-mb)*(p3-ab))
    if (s  +0.001 < s1 + s2 + s3): print("NO")
    else: print("YES")
#not accepted
#precision problem likely