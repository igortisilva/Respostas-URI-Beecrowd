a, b = input().split()
a = int(a)
b = int(b)
r = a-(b*(a//b))
d = a//b
if r < 0:
    
    r = r-b
    d = (a-r)/b
    
print(int(d), r)

