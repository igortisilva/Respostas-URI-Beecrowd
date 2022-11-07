n = int(input())
for x in range(n):
    a = int(input())
    soma = 0
    for y in range(1,a):
        if(a%y == 0):
            soma = soma + y
    if(soma == a):
        print(a, 'eh perfeito')
    else:
        print(a, 'nao eh perfeito')
