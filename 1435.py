saida = int(input())
while (saida != 0):
    matriz = []
    for i in range(saida):
        matriz.append([0]* saida)
    #linha
    count = 0
    fim = saida
    for i in range(count,fim):
        for j in range(count,fim):
            matriz[i][j] = count+1
            matriz[fim-1][j] = count+1
            matriz[j][i] = count+1
            matriz[j][fim-1] = count+1
        fim =fim -1
        count = count+1
    
    for x in range(saida):
        print(end='')
        for y in range(saida):
            if(y == saida-1):
                print('{:3}'.format(matriz[x][y]))
            else:  
                print('{:3}'.format(matriz[x][y]), end=' ')
    print()

    
        
    saida = int(input())
