a = int(input())
b = int(input())
soma = 0
if(a == b):
    print(soma)
else:
    if(a > b):
        count = b+1
        while(count < a):
            if((count%2) != 0):
                soma = soma + count
            count = count+1
    if(b > a):
        count = a+1
        while(count < b):
            if((count%2) != 0):
                soma = soma + count
            count = count+1
    print(soma)
