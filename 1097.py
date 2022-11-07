i = 0
count = 0
j = 1
while(i < 2.02):
    w = j
    for k in range(3):
        if(w == 1 or w == 2 or w == 3.0 or w == 4 or w == 5):
            t = round(w)
        else:
            t = '%.1f'%w
        print('I=%.1f'%i,'J='+str(t))
        w = w+1
    i = i+0.2
    j = j+0.2
   
        
