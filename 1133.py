a = int(input())
b = int(input())
maior = 0
menor = 0
if(a > b):
    maior = a
    menor = b
else:
    menor = a
    maior = b
for x in range(menor+1, maior):
    if((x % 5) == 2 or (x%5) == 3):
        print(x)
