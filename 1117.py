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
