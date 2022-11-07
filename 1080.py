maior = 0
pos = 0
for x in range(1,101):
    a = int(input())
    if(a > maior):
        maior = a
        pos = x
print(maior)
print(pos)
