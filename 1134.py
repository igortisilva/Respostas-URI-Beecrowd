a = int(input())
al = 0
gl = 0
dl = 0
while(a !=4):
    if(a == 1):
        al = al+1
    elif(a==2):
        gl = gl+1
    elif(a ==3):
        dl = dl+1
    a = int(input())
print('MUITO OBRIGADO')
print('Alcool:',al)
print('Gasolina:', gl)
print('Diesel:',dl)
