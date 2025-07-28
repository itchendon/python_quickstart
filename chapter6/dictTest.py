d={
    'name':'zhangsan',
    'age':18,
}
print(d,type(d))  # {'name': 'zhangsan', 'age': 18} <class 'dict'>
# 新增属性
d['height']=180
print(d,type(d))  # {'name': 'zhangsan', 'age': 18, 'height': 180} <class 'dict'>
print(d['name'])

print("***"*10)
for k,v in d.items():
    print(k,v)
print("***"*10)
for k in d:
    print(k,d[k])
print("***"*10)
for v in d.values():
    print(v)



print("*******************字典的常用方法*********************")

print(d.pop("name"))  # zhangsan
print(d)  # {'age': 18, 'height': 180}
a = d.copy()
print(a,type(a))  # {'age': 18, 'height': 180} <class 'dict'>
d.popitem()
print(d,type(d))
# 弹出一个项（包括键值对）
d.popitem()
print(d,type(d))
print(a)
# 清空元素
a.clear()
print(a)