name ="hello"
# 表示重复用说三遍
showName = name *3
print(showName)  # hellohellohello
# 字符串切片
content = "nick name"
print(content[0])
print(content[1])
print(content[2])
print(content[3])
print(content[4])
# 切片包头不包尾，所以需要提取的位置+1
print(content[0:9])  # nick name

numserial = "123456789"
print(numserial[1:10:2]) #2468
# 默认可以不写开始和结束。
print(numserial[::2])  # 13579
#逆序
print(numserial[-1:-10:-2])  # 97531
