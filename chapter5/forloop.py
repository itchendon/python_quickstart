for i in range(10):
    print((i+1),end="")
print()
print(list(range(20)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# 计算阶乘1！+2！+3！+4！
ret = 0
for i in range(20):
    tempRet = 1
    if i>0:
        for j in range(i+1):
            if j>0:
                tempRet *=j;
        print(tempRet)
        ret+=tempRet;
print(ret)
num = 11
for i in range(2,num):
    if num%i==0:
        print("%d不是质数" % (num))
        break
else:
    print("%d是质数" % (num))