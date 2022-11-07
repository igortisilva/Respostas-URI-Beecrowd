a = float(input())
if(a >= 0 and a<=2000):
    print('Isento')
else:
    if(a>2000 and a <=3000):
        t = a - 2000
        t = t*0.08
        print('R$ %.2f'%t)
    else:
        if(a > 3000 and a <=4500):
            t = a - 3000
            t = (1000*0.08) + t*0.18
            print('R$ %.2f'%t)
        else:
            if(a > 4500):
                t = a - 4500
                t = (1000*0.08) + (1500*0.18) + t*0.28
                print('R$ %.2f'%t)
    
