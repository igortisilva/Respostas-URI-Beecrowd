a,a2 = input().split()
a3,a4,a5,a6,a7 = input().split()
a8,a9 = input().split()
a10,a11,a12,a13,a14 = input().split()
dia1 = int(a2)
hora1 = int(a3)
min1 = int(a5)
seg1 = int(a7)
dia2 = int(a9)
hora2 = int(a10)
min2 = int(a12)
seg2 = int(a14)

total1 = (hora1*60)+min1+(seg1/60)
total2 = (hora2*60)+min2+(seg2/60)
total = total1 - total2
if(total1 > total2):
    dia2 = dia2-1
w = (dia2-dia1)*1440 + total
dia = w//1440
if(hora1 >= hora2 and min1 >= min2 and seg1 > seg2):
    horas = hora1 - hora2
    horas = 23-horas
    m = min1 - min2
    minu = 59-m
    segs = 60-(seg1-seg2)
    print(dia,horas,minu,segs)
else:
    mo = hora1 * 60
    mo = mo + min1
    mo = mo +(seg1//60)

    mo2 = hora2 * 60
    mo2 = mo2 + min2
    mo2 = mo2 +(seg2//60)
    
