import sys
c=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
s=str(input())
cap=0
low=0
length=0
num=0
if len(s)<4:
    print("Invalid")
    sys.exit()
for x in range (0,len(s)):
    if s[x].lower() in c:
        continue
    else: 
        print("Invalid")
        sys.exit()
for x in range (0,len(s)):
    try:
        temp=int(s[x])
        num=1
        break
    except:
        pass
if s!=s.lower():
    cap=1
if s!=s.upper():
    low=1
if len(s)>=8:
    length=1
if cap*low*length*num==0:
    print("Weak")
else: print("Strong")