a, b = input().split()
c, d = input().split()
a = float(a)
b = float(b)
c = float(c)
d = float(d)
aa = (c - a)**2
bb = (d - b)**2
aa = aa+bb
aa = aa ** (1/2)
print ('%.4f' % aa)
