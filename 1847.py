a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
if(a>b):
    if(b > c):
        dif = a-b
        dif2 = b-c
        if(dif2 < dif):
            print(':)')
        else:
            print(':(')
    if(c >=b):
        print(':)')
elif(b>a):
    
    if(c > b):
        dif = b-a
        dif2 = c-b
        if(dif2 < dif):
            print(':(')
        else:
            print(':)')
    if(c <= b):
        print(':(')
else:
    if(c>b):
        print(':)')
    else:
        print(':(')
        
