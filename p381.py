def tinhDienTich(xA,yA,xB,yB,xC,yC):
    return 0.5*abs(xA*yB-xB*yA+xB*yC-xC*yB+xC*yA-xA*yC)
xA,yA,xB,yB,xC,yC=[int(i) for i in input().split()]
print("{:.9f}".format(tinhDienTich(xA,yA,xB,yB,xC,yC)))