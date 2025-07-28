import os
# 打开文件
file = open('file.txt',"r",encoding="utf-8")
# 读取文件
content = file.read()
print(content)
# 关闭文件
file.close()
# 获取当前路径
path = os.getcwd();
print(path)
