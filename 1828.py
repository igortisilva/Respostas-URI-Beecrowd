n = int(input())
for x in range(n):
    a,b = input().split()
    v = True
    w = 1
    if(a == 'papel'):
        if(b == 'papel'):
            print('Caso #'+str(x+1)+': De novo!')
            w = 0
        elif(b == 'Spock'):
            v = True
        elif(b == 'pedra'):
            v = True
        else:
            v = False
    elif(a == 'pedra'):
        if(b == 'pedra'):
            print('Caso #'+str(x+1)+': De novo!')
            w = 0
        elif(b == 'lagarto'):
            v = True
        elif(b == 'tesoura'):
            v = True
        else:
            v = False
    elif(a == 'tesoura'):
        if(b == 'tesoura'):
            print('Caso #'+str(x+1)+': De novo!')
            w = 0
        elif(b == 'papel'):
            v = True
        elif(b == 'lagarto'):
            v = True
        else:
            v = False
    elif(a == 'lagarto'):
        if(b == 'lagarto'):
            print('Caso #'+str(x+1)+': De novo!')
            w = 0
        elif(b == 'Spock'):
            v = True
        elif(b == 'papel'):
            v = True
        else:
            v = False
    elif(a == 'Spock'):
        if(b == 'Spock'):
            print('Caso #'+str(x+1)+': De novo!')
            w = 0
        elif(b == 'tesoura'):
            v = True
        elif(b == 'pedra'):
            v = True
        else:
            v = False
    if(v == True and w == 1):
        print('Caso #'+str(x+1)+': Bazinga!')
    elif(v == False and w == 1):
        print('Caso #'+str(x+1)+': Raj trapaceou!')
