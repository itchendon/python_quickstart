# 打开文件
file = open('testWrite.txt', 'w', encoding='utf-8');
content = '''
我在写一段文字
这段文字是多行的
你看看
'''
file.write(content)
appenLines = ["追加一行内容！！！\n","测试\n"]
file.writelines(appenLines)
file.close();