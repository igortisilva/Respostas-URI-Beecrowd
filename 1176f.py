o = int(input())
vet = []
for h in range(o):
    a = int(input())
    ant = 0
    antt = 0
    soma = 0
    for x in range(a+1):
        if(x == 0):
            vet.insert(x,x)
            ant = x
        elif(x == 1):
            antt = x
            vet.insert(x,x)
        else:
            soma = ant + antt
            vet.insert(x,soma)
            ant = antt
            antt = soma
    w = len(vet)
    kk = vet[w-1]
    print('Fib('+str(w-1)+') =', kk)
    vet.clear()
