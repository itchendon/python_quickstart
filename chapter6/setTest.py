s = set()
print(s,type(s)) # set() <class 'set'>
# 允许有重复原酸，但是它会给我们去重的。
s={1,2,3,4,5,4}
print(s,type(s))
# 列表转换成集合
s = set([1,2,3,4,5,4])
print(s,type(s)) # {1, 2, 3, 4, 5} <class 'set'>
# 元组转换成集合
s = set((1,2,3,4,5,4))
print(s,type(s))  # {1, 2, 3, 4, 5} <class 'set'>
# 字符串转换成集合(顺序不确定)
s = set("123456")
print(s,type(s))  # {'1', '3', '4', '6', '2', '5'} <class 'set'>
# 字典赚集合
s = set({1:'a',2:'b',3:'c'})
print(s,type(s)) # {1, 2, 3} <class 'set'>
# in
print(1 in s) # True
print("*******************集合的常用方法******************************")
print(len(s))
print(max(s))
print(min(s))
# 集合不可以使用脚标,会报错TypeError: 'set' object is not subscriptable
# print(s[0])

s.remove(1)
print(s,type(s))  # {2, 3} <class 'set'>
s.update({4,5,6,7,8})
print(s,type(s))  # {2, 3, 4, 5, 6, 7, 8} <class 'set'>
s.add(100)
print(s,type(s)) # {2, 3, 4, 5, 6, 7, 8, 100} <class 'set'>

s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])
# 取交集
print(s1 & s2) # {4, 5, 6}
print(s1 | s2) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print("*******************集合的遍历******************************")
for i in s:
    print(i)
list1 = [50,60,60,70,60,90,99,88]
s3 = set(list1)
for i in s3:
    c = list1.count(i);
    print("得分为%d的学生有%d人"%(i,c))
# 执行结果
'''
得分为99的学生有1人
得分为70的学生有1人
得分为50的学生有1人
得分为88的学生有1人
得分为90的学生有1人
得分为60的学生有3人
'''