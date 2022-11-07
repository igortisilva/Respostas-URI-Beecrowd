a,b = input().split()
a = int(a)
b = int(b)
if(a > 14):
    c = 24 - a
    c = c + b
    print('O JOGO DUROU', c, 'HORA(S)')
elif(a!= 0 and b!=0):
    c = b-a
    print('O JOGO DUROU', c, 'HORA(S)')
else:
    print('O JOGO DUROU 24 HORA(S)')
