n = int(input())
for x in range(n):
    a = int(input())
    count = 0
    for y in range(1,a+1):
        if(a%y==0):
            count = count +1
    if(count == 2):
        print(a, 'eh primo')
    else:
        print(a, 'nao eh primo')
