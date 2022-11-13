import math
ox,oy,mx,my,r=[int(i) for i in input().split()]
mo = math.sqrt((mx-ox)*(mx-ox)+(my-oy)*(my-oy))
if mo>r: print("NO")
else: print("YES")