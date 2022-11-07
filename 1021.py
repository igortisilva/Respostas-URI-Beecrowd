a = float(input())
resto = 0

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

i = resto//(0.50)
resto = resto%(0.50)

j = resto//(0.25)
resto = resto%(0.25)

k = resto//(0.10)
resto = resto%(0.10)


l = resto//(1/20)
resto = resto%(1/20)
x = round(resto,4)

m = x/(0.01)
resto = resto%(1/100)
print('NOTAS:')
print(int(b),'nota(s) de R$ 100.00')
print(int(c),'nota(s) de R$ 50.00')
print(int(d),'nota(s) de R$ 20.00')
print(int(e),'nota(s) de R$ 10.00')
print(int(f),'nota(s) de R$ 5.00')
print(int(g),'nota(s) de R$ 2.00')
print('MOEDAS:')
print(int(h),'moeda(s) de R$ 1.00')
print(int(i),'moeda(s) de R$ 0.50')
print(int(j),'moeda(s) de R$ 0.25')
print(int(k),'moeda(s) de R$ 0.10')
print(int(l),'moeda(s) de R$ 0.05')
print(int(m),'moeda(s) de R$ 0.01')
