a = "hello world"
for i in range(len(a)):
    print(i, a[i],sep="----")


print("----"*20)
print(len(a))
# 统计字符粗o 在字符串a的数量
print(a.count("o"))
# 柴扉字符串
print(a.split(" "))
# 使用#简化字符列表分割开
print("#".join(['111','2222','33333333']))  # 111#2222#33333333
# 查找字符在字符串a中的位置，如果没有找到返回-1
print(a.find("a"))



b="23994832991sfklsdjf##"
n1,n2,n3=0,0,0
for i in b:
    # 数字
    if i.isdigit():
        n1+=1;
    # 字母
    elif i.isalpha():
        n2+=1;
    else: # 符号
        n3+=1;
print(n1,n2,n3)




