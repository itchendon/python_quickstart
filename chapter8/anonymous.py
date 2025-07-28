# 普通写法
def method1(a,b):
    return a+b
print(method1(1,2))

# 匿名函数的写法
fun = lambda a,b: a+b
print(fun(1,2))

# map函数配合lambda实现计算
a =[1,2,3,4,5]
ret = map(lambda x:x**2,a)
print(list(ret)) # [1, 4, 9, 16, 25]

# reduce 累积
from functools import reduce
ret2 = reduce(lambda x,y:x+y,a)
print(ret2) # 15

# filter 过滤
ret3 = filter(lambda x:x%2==0,a) # 去掉奇数
print(list(ret3)) # [2, 4]