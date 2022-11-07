a,b = input().split()
a = int(a)
b = int(b)
while(a > 0 and b > 0):
    soma = 0
    maior = 0
    menor = 0
    if(a > b):
        maior = a
        menor = b
    else:
        maior = b
        menor = a
    for x in range(menor, maior+1):
        soma = soma + x
        print(x, end=' ')
    print('Sum=%.0f'%soma)
    a,b = input().split()
    a = int(a)
    b = int(b)
