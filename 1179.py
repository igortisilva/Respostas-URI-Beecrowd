countpar = 0
countimp = 0
vet1 = []
vet2 = []
for x in range(15):
    a = int(input())
    if(a%2==0):
        vet1.append(a)
        countpar = countpar +1
        if(countpar == 5):
            for i in range(len(vet1)):
                print('par['+str(i)+'] =',vet1[i])
            countpar = 0
            vet1.clear()
    else:
        vet2.append(a)
        countimp = countimp+1
        if(countimp==5):
            for j in range(len(vet2)):
                print('impar['+str(j)+'] =',vet2[j])
            countimp = 0
            vet2.clear()
for j in range(len(vet2)):
    print('impar['+str(j)+'] =',vet2[j])
for i in range(len(vet1)):
    print('par['+str(i)+'] =',vet1[i])

