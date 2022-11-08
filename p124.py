def grade (a):
    if a>10 or a<0: return -1
    elif a>=9: return "A+"
    elif a>=8: return "A"
    elif a>=7: return "B"
    elif a>=6: return "C"
    elif a>=5: return "D"
    else: return "E"
n = int(input())
for x in range(0,n):
    print(grade(float(input())))