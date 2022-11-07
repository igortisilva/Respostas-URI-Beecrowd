a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
aa = a-b
bb = a+b
ab = (bb+abs(aa))/2
cb = ((ab +c )+abs(ab-c))/2
print ('%.0f' %cb + ' eh o maior')
