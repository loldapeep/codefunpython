def pascal(a):
        if a == 1:
            return "1"
        elif a == 2:
            return "1 1"
        elif a == 3:
            return "1 2 1"
        elif a == 4:
            return "1 3 3 1"
        elif a == 5:
            return "1 4 6 4 1"
        elif a == 6:
            return "1 5 10 10 5 1"
        elif a == 7:
            return "1 6 15 20 15 6 1"
        elif a == 8:
            return "1 7 21 35 35 21 7 1"
        elif a == 9:
            return "1 8 28 56 70 56 28 8 1"
        elif a == 10:
            return "1 9 36 84 126 126 84 36 9 1"
for x in range (0,int(input())):
    print(pascal(x+1))