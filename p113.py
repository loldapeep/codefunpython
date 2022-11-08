import math
def mien(x,y):
    if x > 0 and y > 0: return 1
    elif x < 0 and y > 0: return 2 
    elif (x < 0 and y < 0): return 3 
    elif (x > 0 and y < 0): return 4 
    elif (x == 0 and y > 0): return 12 
    elif (y == 0 and x < 0): return 23 
    elif (x == 0 and y < 0): return 34 
    elif (y == 0 and x > 0): return 41 
    elif (x == 0 and y == 0): return 1234 
    return 0 
def isin(ax,ay,bx,by,cx,cy,mx,my):
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
    if (s + 0.001 < s1 + s2 + s3): return 0
    else: return 1
ax,ay,bx,by,cx,cy=[int(i) for i in input().split()]

if (ax == 0 and ay == 0): 
    if (bx <= 0): print(1)
    elif (bx >= 5): print(2)
    elif (bx == 1): print(1)
    elif (bx == 4): print(2)
    elif (bx == 2):
        if (by > 0): print(1)
        else: print(2)
elif(mien(ax,ay)==1234 or mien(bx,by)==1234 or mien(cx,cy)==1234): print(4)
elif (isin(ax,ay,bx,by,cx,cy,0,0)==1): print(4)
elif (mien(ax,ay) < 5 and mien(bx,by) < 5 and mien(cx,cy) < 5):
    if (mien(ax,ay)==mien(bx,by) and mien(ax,ay)==mien(cx,cy)): print(1)
    elif (mien(ax,ay)!=mien(bx,by) and mien(ax,ay)!=mien(cx,cy) and mien(cx,cy)!=mien(bx,by)): print(3)
    elif (mien(ax,ay) == mien(bx,by) and mien(ax,ay) != mien(cx,cy)):
        if (mien(ax,ay) == 1):
            if (mien(cx,cy) == 2 or mien(cx,cy) == 4): print(2)
            elif(mien(cx,cy) == 3): print(3)
        elif(mien(ax,ay) == 2):
            if (mien(cx,cy) == 3 or mien(cx,cy) == 1): print(2)
            elif (mien(cx,cy) == 4): print(3)
        elif (mien(ax,ay) == 3): 
            if (mien(cx,cy) == 2 or mien(cx,cy) == 4): print(2)
            elif (mien(cx,cy) == 1): print(3)
        elif (mien(ax,ay) == 4): 
            if (mien(cx,cy) == 3 or mien(cx,cy) == 1): print(2)
            elif (mien(cx,cy) == 2): print(2)
    elif (mien(ax,ay)==mien(cx,cy) and mien(ax,ay)!=mien(bx,by)): 
        if (mien(ax,ay) == 1):
            if (mien(bx,by) == 2 or mien(bx,by) == 4): print(2)
            elif (mien(bx,by) == 3): print(3)
        elif (mien(ax,ay) == 2): 
            if (mien(bx,by) == 3 or mien(bx,by) == 1): print(2)
            elif (mien(bx,by) == 4): print(3)
        elif (mien(ax,ay) == 3): 
            if (mien(bx,by) == 2 or mien(bx,by) == 4): print(2)
            elif (mien(bx,by) == 1): print(3)            
        elif (mien(ax,ay) == 4): 
            if (mien(bx,by) == 3 or mien(bx,by) == 1): print(2)
            elif (mien(bx,by) == 2): print(3)
    elif (mien(bx,by)==mien(cx,cy) and mien(bx,by)!=mien(ax,ay)):
        if (mien(bx,by) == 1):
            if (mien(ax,ay) == 2 or mien(ax,ay) == 4): print(2)
            elif (mien(ax,ay) == 3): print(3)           
        elif (mien(bx,by) == 2): 
            if (mien(ax,ay) == 3 or mien(ax,ay) == 1): print(2)
            elif (mien(ax,ay) == 4): print(3)            
        elif (mien(bx,by) == 3): 
            if (mien(ax,ay) == 2 or mien(ax,ay) == 4): print(2)
            elif (mien(ax,ay) == 1): print(3)
        elif (mien(bx,by) == 4): 
            if (mien(ax,ay) == 3 or mien(ax,ay) == 1): print(2)
            elif (mien(ax,ay) == 2): print(3)
            