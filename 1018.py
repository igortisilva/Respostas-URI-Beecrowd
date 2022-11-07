a = int(input())
resto = 0
print(a)
b = a//100
resto = a%100


c = resto//50
resto = resto%50

d = resto//20
resto = resto%20

e = resto//10
resto = resto%10

f = resto//5
resto = resto%5

g = resto//2
resto = resto%2

h = resto//1
resto = resto%1
print(b,'nota(s) de R$ 100,00')
print(c,'nota(s) de R$ 50,00')
print(d,'nota(s) de R$ 20,00')
print(e,'nota(s) de R$ 10,00')
print(f,'nota(s) de R$ 5,00')
print(g,'nota(s) de R$ 2,00')
print(h,'nota(s) de R$ 1,00')
