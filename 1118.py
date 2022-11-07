op = 1
while(op != 2):
    if(op == 1):
        count = 0
        soma = 0
        while(count < 2):
            a = float(input())
            if(a >= 0 and a <=10):
                soma = soma + a
                count = count +1
            else:
                print('nota invalida')
        media = soma/2
        print('media = %.2f'%media)
    print('novo calculo (1-sim 2-nao)')
    op = int(input())
