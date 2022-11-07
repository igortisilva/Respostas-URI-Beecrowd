a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
if (a > b and a > c):
    if(b>c):
        print(c)
        print(b)
    else:
        print(b)
        print(c)
    print(a)
elif(b > a and b > c):
    if(a>c):
        print(c)
        print(a)
    else:
        print(a)
        print(c)
    print(b)
elif(c > a and c > b):
    if(a>b):
        print(b)
        print(a)
    else:
        print(a)
        print(b)
    print(c)

print('\n'+str(a))
print(b)
print(c)
