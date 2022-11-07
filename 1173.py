
a = int(input())
x = [a,0,0,0,0,0,0,0,0,0]
for y in range(1,10):
    w = y-1
    x[y] = x[w]*2
for j in range(10):
    print('N['+str(j)+'] =', x[j])
