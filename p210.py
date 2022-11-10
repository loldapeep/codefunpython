s=str(input())
c = 1 ; m = 0 ; d = 0 ; kq = 0 ; e = 0 ; f = 1 ; n = 0
for i in range (0,len(s)):
    if (s[i]=='D'):
        d+=1
        x = i
    if (i < len(s)-1):
        if (s[i]=='D' and s[i+1]=='D'): c+=1
        else: c = 1
    if (c > m):
        m = c
        y = i - m + 2
if (d == 0): kq = kq + 0
elif (d == 1):
    kq = kq + 1
    #s.erase(x,1)
    #s=s[:x]+s[(x+1):]
    if x+1>=len(s):
        s=s[:x]
    else: s=s[:x]+s[(x+1):]
else:
    kq = kq + m
    #s.erase(y,m)
    if y+m>=len(s):
        s=s[:y]
    else: s=s[:y]+s[y+m:]
for i in range (0,len(s)):
    if (s[i]=='D'): e+=1
    if (i < len(s)-1):
        if (s[i]=='D' and s[i+1]=='D'): f+=1
        else: f = 1
    if (f > n): n = f
if (e == 0): kq = kq + 0
elif (e == 1): kq = kq + 1
else: kq = kq + n
print(kq)
#tle
#not accepted