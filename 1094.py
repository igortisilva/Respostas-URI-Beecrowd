a = int(input())
c = 0
r = 0
s = 0
for x in range(a):
    i,j= input().split()
    i = int(i)
    if(j == 'C'):
        c = c+i
    elif(j == 'S'):
        s = s+i
    else:
        r = r+i
total = r+s+c
por1 = (100.0*r)/total
por2 = (100.0*s)/total
por3 = (100.0*c)/total
print('Total:',total,'cobaias')
print('Total de coelhos:',c)
print('Total de ratos:',r)
print('Total de sapos:',s)
print('Percentual de coelhos: %.2f'%por3,'%')
print('Percentual de ratos: %.2f'%por1,'%')
print('Percentual de sapos: %.2f'%por2,'%')
        
    
