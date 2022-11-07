x = []
vet = []
for w in range(20):
    a =int(input())
    x.append(a)
    vet.append(0)
for e in range(10):
    vet[e] = x[19-e]
    vet[19-e] = x[e]
for y in range(len(vet)):
    print('N['+str(y)+'] =',vet[y])
