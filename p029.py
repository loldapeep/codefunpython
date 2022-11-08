a, b, c = map(float, input().split())
if a+b>c and a+c>b and b+c>a:
   if a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
       s = 0
   elif a*a > b*b+c*c or b*b > a*a+c*c or c*c > a*a+b*b:   
       s = 2
   else:
       s = 1
print(s)