matriz = []
letra = input()
for i in range(12):
    matriz.append([0]*12)
    for j in range(12):
        matriz[i][j] = float(input())
result = 0
count = 0
div = 0

for k in range(1,6):
    for l in range(11-count,12):
        result = result + matriz[k][l]
        div = div+1
    count = count +1
count = 0
for o in range(6,11):
    for p in range(7+count,12):
        result = result + matriz[o][p]
        div = div+1
    count = count +1

if(letra == 'M'):
    result = result/div
print('%.1f'%result)

