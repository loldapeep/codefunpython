def late (a,b):
    if a<7:
        return False
    elif a == 7:
        if b<6:
            return False
        else: return True
    else: return True
count=0
for x in range (0,6):
    a,b = [int(i) for i in input().split()]
    if late(a,b): count+=1
if count>2:
    print(":'(")
else: print(":)")