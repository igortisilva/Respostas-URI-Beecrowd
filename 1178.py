vet = []
a = float(input())
for x in range(100):
    vet.append(a)
    a = a/2
    print('N['+str(x)+'] = %.4f'%vet[x])
