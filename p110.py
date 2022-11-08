import math
def time(a,b,c,d):
    displace = c*a
    time1=(d-displace)/a
    time2=d/b
    timechase=displace/(b-a)
    if time2>=time1:
        return abs(math.ceil(time1-timechase))
    else:
        return abs(math.floor(time2-timechase))
v1,v2,t,d = [float(i) for i in input().split()]
if v1>=v2:
    print("INF")
else:
    print(time(v1,v2,t,d))