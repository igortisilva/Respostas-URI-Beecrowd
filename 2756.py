vetor = ['A', 'B', 'C', 'D', 'E']
esp = 7
tamanho = vetor.__len__()
saida = ''
i = 0
for j in range(esp):
    saida = saida + ' '
saida = saida + vetor[i]
print (saida)
saida = ''
esp -=1
i +=1
for x in range(1, 9, 2):
    for j in range(esp):
        saida = saida + ' '
    saida = saida + vetor[i]
    for k in range(x):
        saida = saida + ' '
    saida = saida + vetor[i]
    print (saida)
    saida = ''
    esp -=1
    i +=1
i-=2
esp+=2
for x in range(5, -1, -2):
    for j in range(esp):
        saida = saida + ' '
    saida = saida + vetor[i]
    for k in range(x):
        saida = saida + ' '
    saida = saida + vetor[i]
    print (saida)
    saida = ''
    esp +=1
    i -=1
for j in range(esp):
    saida = saida + ' '
saida = saida + vetor[i]
print (saida)
