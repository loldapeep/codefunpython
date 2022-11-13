n=int(input())
t=1
s=0
for i in range (1,n+1):
    t*=i
    t%=1000
    s+=t
    s%=1000
if s<10: print(f"000{s}")
elif s<100: print(f"00{s}")
elif s<1000: print(f"0{s}")
else: print(s)