media = 0
saida = int(input())
count = 0
while(saida >= 0):
    count = count +1
    media = saida +media
    saida = int(input())
media = media/count
print('%.2f'%media)
    
