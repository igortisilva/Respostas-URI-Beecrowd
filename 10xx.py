a = float(input())
s = 0
b = 0
p = 0
if(a <= 400):
    p = 15
    b = a*0.15
    s = a+b
elif(a > 400 and a<=800):
    p=12
    b = a*0.12
    s = a+b
elif(a > 800 and a<=1200):
    p=10
    b = a*0.10
    s = a+b
elif(a > 1200 and a<=2000):
    p=7
    b = a*0.07
    s = a+b
else:
    p=4
    b = a*0.04
    s = a+b
print('Novo salario: %.2f'%s)
print('Reajuste ganho: %.2f'%b)
print('Em percentual:',p,'%')
