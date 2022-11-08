import math
a = math.floor(float(input()))
if 0<=a and a<50:
    b=a*2
    if b>100:
        print("Break the Mac")
    else:
        print(b)
elif 100>=a and a>70:
    print(0)
else:
    print("Break the Mac")