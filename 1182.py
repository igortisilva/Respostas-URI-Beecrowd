matriz = []
l = int(input())
letra = input()
for i in range(12):
    matriz.append([0]*12)
    for j in range(12):
        matriz[i][j] = float(input())
result = 0
for k in range(12):
    result = result + matriz[k][l]
if(letra == 'M'):
    result = result/12
print('%.1f'%result)

