a,b,c,d = input().split()
a= float(a)
b= float(b)
c= float(c)
d= float(d)
a =a*2
b=b*3
c=c*4
d=d*1
m = (a+b+c+d)/10
print('Media: %.1f'% m)
if(m >= 7.0):
    print('Aluno aprovado.')
elif(m < 7.0 and m >= 5.0):
    print('Aluno em exame.')
    e = float(input())
    
    print('Nota do exame: %.1f'%e)
    mf = (e+m)/2
    if(mf >= 5.0):
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: %.1f'%mf)
else:
    print('Aluno reprovado.')
