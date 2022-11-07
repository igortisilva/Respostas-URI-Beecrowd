a = int(input())
horas = 0
minutos = a//60
segundos = a%60

if(minutos >= 60):
    horas = minutos//60
    minutos = minutos%60
print(str(horas)+':'+str(minutos)+':'+str(segundos))
