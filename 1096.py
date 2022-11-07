i = 1
count = 0
for x in range(1,10):
    j = 7
    if(x%2 != 0):
        for k in range(3):
            print('I='+str(i)+' J='+str(j))
            j = j-1
        i = i+2
        
