a,b = input().split()
a=int(a)
b =int(b)
count = 1
for x in range(1,b+1):
    if(count !=a):
        if(x == b):
            print(x, end='')
        else:
            print(x, end=' ')
    else:
        print(x)
        count = 0
    count = count +1
