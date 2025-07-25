tp_info=(1,2,3,4,5,"张三","李四",20,22)
print(tp_info)
print(type(tp_info))
# 如果只有一个元素的时候打出来的类型就是那个元素的类型，如果要打出来的类型是元组，就需要在那个元素的后面添加一个逗号tp2 = (1,)
tp2 = (1)
print(tp2)  # 1
print(type(tp2))  # <class 'int'><class 'int'>

tp3 = tuple("hello world") # str-->tuple
print(tp3) # ('h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd')

tp4 = tuple([1,2,4])
print(tp4,type(tp4)) # (1, 2, 4) <class 'tuple'>

list1 = list(tp4) # tuple--->list
print(list1,type(list1)) # [1, 2, 4] <class 'list'>

print(str(tp4),type(str(tp4))) # (1, 2, 4) <class 'str'>


tp5 = tuple([1,2,3,4,5,6,7,8,9])
print(max(tp5))
print(len(tp5))
print(min(tp5))
print(tp5[-1])
# 切片
print(tp5[1::2]) #(2, 4, 6, 8)

print(tp5+tp4)
print(tp5*5)  # (1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# TypeError: 'tuple' object does not support item assignment
# 元组不支持修改
# tp5[1]=22

# 元组的方法
tp6=(1,2,3,4,5,6,7,8,9,4)
# 统计元组里面有几个4
print(tp6.count(4))  # 2
# 计算4的元素在元组的位置(脚标)
print(tp6.index(4)) # 3