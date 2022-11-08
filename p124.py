import sys
def grade (a):
    if a>10 or a<0: return -1
    elif a>=9: return "A+"
    elif a>=8: return "A"
    elif a>=7: return "B"
    elif a>=6: return "C"
    elif a>=5: return "D"
    else: return "E"
n = int(input())
def loopinput(a):
    try: 
        a[0] = int(input())
        return True
    except:
        return False
a=[0]
while loopinput(a):
    print(grade(a[0]))
    #not accepted
    #EOF exception?