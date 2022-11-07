a= int(input())
count = 0
ins = 0
outs = 0
while(count < a):
    x = int(input())
    if(x >= 10 and x <=20):
        ins = ins+1
    else:
        outs = outs+1
    count = count+1
print(ins,'in')
print(outs,'out')
