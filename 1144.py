a = int(input())
count = 1
for x in range(a):
    mult = count*count
    ult = mult*count
    print(count,mult,ult)
    print(count, mult+1,ult+1)
    count = count +1
    
