a,b,c = input().split()
a = float(a)
b = float(b)
c = float(c)
tra = False
if(abs(b-c)< a and a < (b+c)):
    if(abs(a-c)< b and b < (a+c)):
        if(abs(a-b)< c and c < (b+a)):
            tra = True
if(tra == True):
    print('Perimetro =',(a+b+c))
else:
    t = ((a+b)*c)/2
    print('Area =', t)
