a = int(input())
for x in range(a):
    b,c = input().split()
    b= int(b)
    c = float(c)
    result = 0
    if(c == 0):
        print('divisao impossivel')
    else:
        result = b/c
        print('%.1f'%result)
