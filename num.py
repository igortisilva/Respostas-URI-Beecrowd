
telefone = input("Digite")
numero = telefone.split('-')

if(len(numero) > 1):
    saida = numero[0] + numero[1]
    numero[0] = saida

if(len(numero[0]) == 7):
    numero[0] = '3'+numero[0]

print(f'{numero[0]}')
print(f'{numero[0][:4]}-{numero[0][4:]}')
