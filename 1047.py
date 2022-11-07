a,b,c,d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
if(a == c and b == d):
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    if(a >= c and b> d):
        x = a
        y = c
        z = x - y
        h = 23-z
        m = 0
        if(b > d):
            m = 60 - (b-d)
        else:
            m = 60 -(d-b)
        print('O JOGO DUROU', h,'HORA(S) E', m,'MINUTO(S)')
    else:
        x = a * 60
        x = x + b
        y = c * 60
        y = y + d
        if(x<y):
            w = y-x
            h = w//60
            m = w%60   
            print('O JOGO DUROU', h,'HORA(S) E', m,'MINUTO(S)')
        else:
            w = x-y
            h = w//60
            m = w%60     
            print('O JOGO DUROU', h,'HORA(S) E',m,'MINUTO(S)')
