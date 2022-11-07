saida = int(input())
while(saida != 0):
    count = 0
    soma = 0
    while(count != 5):
        if(saida%2==0):
            soma = soma + saida
            count = count+1
        saida = saida +1
    print(soma)
    saida = int(input())
