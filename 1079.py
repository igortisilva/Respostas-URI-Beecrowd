a = int(input())
for x in range(a):
    b,c,d = input().split()
    b = float(b)
    c = float(c)
    d = float(d)
    t = (b*0.2+c*0.3+d*0.5)
    print('%.1f'%t)
