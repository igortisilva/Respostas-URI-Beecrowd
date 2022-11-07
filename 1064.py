count = 0
a = float(input())
b = float(input())
c = float(input())
d= float(input())
e = float(input())
f = float(input())
media = 0
if(a> 0):
    count = count +1
    media = media+a
if(b> 0):
    count = count +1
    media = media+b
if(c> 0):
    count = count +1
    media = media+c
if(d> 0):
    count = count +1
    media = media+d
if(e> 0):
    count = count +1
    media = media+e
if(f> 0):
    count = count +1
    media = media+f
media = media/count
print(count,'valores positivos')
print('%.1f'%media)
