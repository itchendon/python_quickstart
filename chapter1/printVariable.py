number=5000000
print(number)
content="卧槽"
print(content)

print("2025","年-07","月-25日",sep="",end="。")

print()
#%02d表示如果要占两位，如果不够要使用0来替代
print("今天是%d年%02d月%d日%s,风速%.2f米/s" % (2025,7,24,",今天是个好日子！！",3.145))