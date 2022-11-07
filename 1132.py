a = int(input())
b = int(input())
maior = 0
menor = 0
if(a > b):
    maior = a
    menor = b
else:
    menor = a
    maior = b
soma = 0
for x in range(menor, maior+1):
    if((x % 13) != 0):
        soma = soma+x
print(soma)
