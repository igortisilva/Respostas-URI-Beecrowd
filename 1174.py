x = []
for w in range(100):
    a =float(input())
    x.append(a)
for y in range(len(x)):
    if(x[y] <=10):
        print('A['+str(y)+'] = %.1f'%x[y])
