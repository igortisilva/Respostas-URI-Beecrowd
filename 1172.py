x = []
for w in range(10):
    a =int(input())
    x.append(a)
for y in range(len(x)):
    if(x[y] <=0):
        x[y] = 1
    print('X['+str(y)+'] =',x[y])
