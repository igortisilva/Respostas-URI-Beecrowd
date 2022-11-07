saida = int(input())
while (saida != 0):
    matriz = []
    for i in range(saida):
        matriz.append([0]* saida)
    #linha
    count = 1
    ini = 0
    fim = saida
    for i in range(fim):
        for j in range(fim):
            count = 1+i
            if(i == j):
                matriz[i][j]=1
                w = 1
                for x in range(count,fim):
                   matriz[ini][x] = w+1
                   matriz[x][ini] = w+1
                   w = w+1
                count = count+1
                ini = ini+1
            
               
    
    for x in range(saida):
        print(end='')
        for y in range(saida):
            if(y == saida-1):
                print('{:3}'.format(matriz[x][y]))
            else:  
                print('{:3}'.format(matriz[x][y]), end=' ')
    print()

    
        
    saida = int(input())
