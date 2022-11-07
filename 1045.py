x,y,z = input().split()
x = float(x)
y = float(y)
z = float(z)
a = 0.0
b= 0.0
c =0.0
if(x > y and x > z):
    a = x
    b= y
    c = z
if(y > x and y > z):
    a = y
    b =x
    c=z
else:
    a = z
    b = x
    c=y
if(a >=(b+c)):
    print('NAO FORMA TRIANGULO')
else:
    a2 = a**2
    b2 = b**2
    c2 = c**2
    if(a2 == (b2+c2)):
        print('TRIANGULO RETANGULO')
    elif(a2 > (b2+c2)):
        print('TRIANGULO OBTUSANGULO')
    elif(a2 < (b2+c2)):
        print('TRIANGULO ACUTANGULO')
    if(a == b and a==c):
        print('TRIANGULO EQUILATERO')
    elif(a == b or a ==c or c ==b):
        print('TRIANGULO ISOSCELES')
