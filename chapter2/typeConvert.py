s = "2025"
v = int(s)
print(type(s),type(v),v)
s2 = "3.14"
# 数值类型的转换可以互相转换，包含小鼠点包含小数点的字符串和数值不可以直接转换
f1 = float(s2)
v2 = int(f1)

b1,b2 =True,False
print(type(b1),type(b2),int(b1),int(b2))