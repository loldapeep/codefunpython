def display(n):
    fn=1; f0=0;f1=1;f2=1
    sum=0
    for x in range (0,n-2):
        fn=f0+f1+f2
        f0=f1
        f1=f2
        f2=fn
    print(fn)
display(int(input()))