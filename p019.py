import sys
def loopinput(n):
    try: 
        n[0] = int(input())
        return True
    except:
        return False
n=[0]
while loopinput(n):
    if n[0]==19:
        print(19)
        sys.exit()
print("IMPOSSIBLE")