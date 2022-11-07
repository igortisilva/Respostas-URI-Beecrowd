a = 0
b = 0
count = 0
while(count !=2):
    if(count == 0):
        a = int(input())
        count = count +1
    elif(count == 1):
        x = int(input())
        if(x > a):
            b = x
            count = count +1
saida = 0
cont = 0
while(saida < b):
    saida = saida + (a + cont)
    cont = cont + 1
print(cont)

        
