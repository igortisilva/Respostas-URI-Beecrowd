a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
par = 0
impar = 0
pos = 0
neg = 0
if((a%2)== 0):
    par = par+1
else:
    impar = impar+1
if((b%2)== 0):
    par = par+1
else:
    impar = impar+1
if((c%2)== 0):
    par = par+1
else:
    impar = impar+1
if((d%2)== 0):
    par = par+1
else:
    impar = impar+1
if((e%2)== 0):
    par = par+1
else:
    impar = impar+1
if(a > 0):
    pos = pos+1
elif(a < 0):
    neg = neg +1
if(b > 0):
    pos = pos+1
elif(b < 0):
    neg = neg +1
if(c > 0):
    pos = pos+1
elif(c < 0):
    neg = neg +1
if(d > 0):
    pos = pos+1
elif(d < 0):
    neg = neg +1
if(e > 0):
    pos = pos+1
elif(e < 0):
    neg = neg +1
print(par,'valor(es) par(es)')
print(impar,'valor(es) impar(es)')
print(pos,'valor(es) positivo(s)')
print(neg,'valor(es) negativo(s)')
