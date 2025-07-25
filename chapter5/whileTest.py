n=0
while n<10:
    print("%d - hello world"%(n+1))
    n+=1
num=12
a=2;
isPrimeNumber=True
while a<num:
    if num%a==0:
        print("%d不是质数"%(num))
        isPrimeNumber=False
        break
    a += 1
else:
# if isPrimeNumber:
    print("%d是质数"%(num))



