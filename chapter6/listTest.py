list1 = [];
list2 = ["张三",25];
print(type(list1))
print(list2)
# 只能将字符串转换成为list，其他类型都不可以 ，list()函数只能有一个参数
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']
list3 = list("123456789")
print(list3)  # ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# 9
print(list3[-1])
# 切片
print(list3[0::2])  # ['1', '3', '5', '7', '9']
# 重复
print(list3*2) # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("1" not in list3)  # False
print("1" in list3)  # True


print(len(list3))
print(max(list3))
print(min(list3))
# 删除变量
# del list3
# 变量被删除了，再次使用会报错。
# print(list3)
for item in list3:
    print(item,sep="",end="-")
print()
# 美剧，i表示脚标，j表示值
for i,j in enumerate(list3):
    print(i,j)
print("*"*30)
# 添加函数
list3.append("demo")
print(list3)
list3.extend(['kk','vv','dd'])
print(list3)
# 在第一个位置插入一个元素100
list3.insert(0,100)
print(list3)
list3.remove(100)
print(list3)
# 清空所有的元素
list3.clear();
print(list3)

personAge = [23,24,22,27,31,63,28]
print(sum(personAge))
print(sum(personAge)/len(personAge))