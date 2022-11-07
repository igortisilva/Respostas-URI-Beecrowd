matriz = []
letra = input()
for i in range(12):
    matriz.append([0]*12)
    for j in range(12):
        matriz[i][j] = float(input())
result = 0
count = 1
div = 0

for k in range(12):
    for l in range(12-count):
        result = result + matriz[k][l]
        div = div+1
    count = count +1
if(letra == 'M'):
    result = result/div
print('%.1f'%result)

