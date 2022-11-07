a, b, c = input().split()
a2, b2, c2 = input().split()
b = int(b)
c = float(c)
d = c*b
b2 = int(b2)
c2 = float(c2)
d2 = c2*b2
d = d+d2
print ('VALOR A PAGAR: R$ ' + '%.2f' % d)
