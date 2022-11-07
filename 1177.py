a = int(input())
count = 0
vet = []
for x in range(1000):
    vet.append(count)
    count = count+1
    if(count >= a):
        count = 0
    print('N['+str(x)+'] =',vet[x])
