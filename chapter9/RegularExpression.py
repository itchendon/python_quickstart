import re
result = re.match(r"\d+",'123456789')  # 一定要加个r，表示是正则表达式，否则不认识
print(result)  # <re.Match object; span=(0, 9), match='123456789'> 表示匹配到，了。从0 一直到9的位置

# \w:匹配字母数字下划线
result2 = re.match(r"\w+",'_q1')  # 一定要加个r，表示是正则表达式，否则不认识
print(result2)  # <re.Match object; span=(0, 3), match='_q1'>

# \s:空白字符
result3 = re.match(r"\s+$",' ')
print(result3)
# . 任意字符
result4 = re.match(r"^nmmp\d-\d-\d-.+$",'nmmp5-3-1-hahaha')  # <re.Match object; span=(0, 16), match='nmmp5-3-1-hahaha'>
print(result4)

# []区间，可选列表
result5 = re.match( r'^[abcd]+$',  'aabbbcd')  # <re.Match object; span=(0, 7), match='aabbbcd'>

print(result5)

# | 或者

result6 = re.match( r'^a|b|c$', 'abc') # <re.Match object; span=(0, 1), match='a'>
print(result6)

# 身份证
result7 = re.match( r'^\d{6}((20[0123][0123456789])|(1[89]\d{2}))\d{7}(\d|X)', "12335419916597145X") # <re.Match object; span=(0, 18), match='12335464576597145X'>
print(result7)

result8 =  re.match(r'^20[0123][0123456789]','2025')
print(result8) # <re.Match object; span=(0, 4), match='2025'>
result9 = re.match(r'^1[89]\d{2}','1992')
print(result9) # <re.Match object; span=(0, 4), match='1992'>



# 验证手机号码
phone='18039306932'
result10 = re.match(r'^1\d{10}',phone)
print(result10)  # <re.Match object; span=(0, 11), match='18039306932'>