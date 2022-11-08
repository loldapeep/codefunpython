x1,y1=[int(i) for i in input().split()]
x2,y2=[int(i) for i in input().split()]
x3,y3=[int(i) for i in input().split()]
x4,y4=[int(i) for i in input().split()]
x,y=[int(i) for i in input().split()]
sum = x+y+x1+y1+x2+y2+x3+y3+x4+y4
def mod(m,n):
    if m*n<0:
        return m%n-n
    else: return m%n
def check():
    if mod(sum,16)==-9: return "not outside"
    elif sum%4>=2: return "outside"
    elif mod(sum,8)==4: return "not outside"
    elif mod(sum,16)==8: return "not outside"
    elif mod(sum,16)==9: return "outside"
    elif mod(sum,3)==0: return "outside"
    else: return "not outside"
print(check())