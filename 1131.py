saida = 1
vg = 0
vi = 0
emp = 0
count = 0
while(saida == 1):
    a,b =input().split()
    a = int(a)
    b = int(b)
    count = count +1
    if(a > b):
        vi = vi + 1
    elif(b > a):
        vg = vg + 1
    else:
        emp = emp +1
    print('Novo grenal (1-sim 2-nao)')
    saida = int(input())
print(count,'grenais')
print('Inter:%.0f'%vi)
print('Gremio:%.0f'%vg)
print('Empates:%.0f'%emp)
if(vi > vg):
    print('Inter venceu mais')
elif(vg > vi):
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')
