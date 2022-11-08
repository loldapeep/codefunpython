def display(n):
    if n<10:
        return "0"+str(n)
    else:
        return str(n)
a=int(input())
h=a//3600
a-=h*3600
m=a//60
a-=m*60
print(display(h)+":"+display(m)+":"+display(a))