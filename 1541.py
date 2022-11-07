import math
while True:
    w = [int(i) for i in input().split()]
    a = 0
    b = 0
    c = 0
    count = 0
    a = w[0]
    if(a == 0):
        break
    b = w[1]
    c = w[2]
    count = count+1
    raiz = (a*b)/(c*0.01)
    raiz = raiz**(1/2)
    print(math.trunc(raiz))


    
    



    
    
