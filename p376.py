a,b,c=[int(i) for i in input().split()]
if (a * a + b * b > c * c and b * b + c * c > a * a and c * c + a * a > b * b ): print("ACUTE")
elif(a * a + b * b == c * c or b * b + c * c == a * a or c * c + a * a == b * b): print("RIGHT")
if (a * a + b * b < c * c or b * b + c * c < a * a or c * c + a * a < b * b): print("OBTUSE")