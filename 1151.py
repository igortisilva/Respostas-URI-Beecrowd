a = int(input())
ant = 0
antt = 0
soma = 0
for x in range(a):
    if(x == 0):
        print(x, end='')
        if(a > 1):
            print(end=' ')
        ant = x
    elif(x == 1):
        antt = x
        print(x, end='')
        if(a > 2):
            print(end=' ')
    else:
        soma = ant + antt
        print(soma, end='')
        if(x != a -1):
            print(end=' ')
        else:
            print('')
        ant = antt
        antt = soma
        
    

