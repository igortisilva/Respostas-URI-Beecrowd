a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
menor = 0
meio = 0
maior = 0
if(a > b):
    if(a>c):
        maior = a
        if(b > c):
            meio = b
            menor = c
    else:
        maior = c
        meio = a
        menor = b
elif(b > c):
    maior = b
    if(c > a):
        meio = c
        menor = a
    else:
        menor = c
        meio = a
elif(c > a):
    maior = c
    meio = b
    menor = a
print(menor)
print(meio)
print(maior)
print()
print(a)
print(b)
print(c)
