a = int(input())
count = 1
result = 0
string = ''
while(count <=a):
    if((count%2)==0):
        result = count ** 2
        string = str(count)+'^2 ='
        print(string,result)
    count = count+1
