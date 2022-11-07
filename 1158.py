n = int(input())

for x in range(n):
    a,b = input().split()
    a = int(a)
    b = int(b)
    soma = 0
    while(b !=0):
        if(a%2!=0):
            soma = soma + a
            b = b-1
        a = a+1
    print(soma)
        
