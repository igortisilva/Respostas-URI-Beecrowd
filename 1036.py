a,b,c = input().split()
a = float(a)
b = float(b)
c = float(c)
x = 2*a
delta = (b**2)-4*a*c
if((x) == 0 or delta < 0):
    print('Impossivel calcular')
else:
    result1 = (-b + (delta**(1/2)))/(x)
    result2 = (-b -(delta**(1/2)))/(x)
    print('R1 = %.5f' % result1)
    print('R2 = %.5f' % result2)
