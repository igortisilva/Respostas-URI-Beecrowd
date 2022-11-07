#a-97 z-122 A-65 Z-90

word = input("Digite")

num = int(input("Digite2"))

lista = []

wordf = ""

for char in word:
    lista.append(ord(char))

print(lista)
for i in range(len(lista)):
    if(lista[i] >= 97):
        lista[i] += num
        if(lista[i] > 122):
            lista[i] -= 26
        if(lista[i] < 97):
            lista[i] += 26
    else:
        lista[i] += num
        if(lista[i] > 90):
            lista[i] -= 26
        if(lista[i] < 65):
            lista[i] += 26
            
for i in lista:
    wordf += chr(i)
print(wordf)
