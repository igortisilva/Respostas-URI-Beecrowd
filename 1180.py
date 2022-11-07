a = int(input())
b = [int(i) for i in input().split()]
menor = b[0]
pos = 0
for j in range(1, len(b)):
    if(menor > b[j]):
        menor = b[j]
        pos = j
print('Menor valor:', menor)
print('Posicao:', pos)
