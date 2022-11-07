x = [int(i) for i in input().split()]
a = 0
b = 0
count = 0
soma = 0
for i in range(len(x)):
    if(x[i] > 0 and count == 0):
        a = x[i]
        count = count +1
    elif(x[i] > 0 and count == 1):
        b = x[i]
        count = count +1

for j in range(0, b):
    soma = soma+a+j
print(soma)
