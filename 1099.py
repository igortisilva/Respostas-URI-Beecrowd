a = int(input())
while(a > 0):
    b,c=input().split()
    b = int(b)
    c = int(c)
    maior = 0
    menor = 0
    soma = 0
    if(b > c):
        maior = b
        menor =c
    else:
        maior = c
        menor = b
    for x in range(menor+1,maior):
        if((x % 2) != 0):
            soma = soma + x
    print(soma)
    a = a - 1
