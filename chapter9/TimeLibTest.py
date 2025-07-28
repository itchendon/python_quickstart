import time
# 从1970年到现在的所有的时间的秒数
time1 = time.time()
print(time1)
# 结构化的时间
time2 = time.localtime();
print(time2)
print(time2.tm_year,type(time2.tm_year))
# 这里输入的时间必须是结构化的时间
time3 = time.strftime('%Y/%m/%d %H:%M:%S',time2)
print(time3) # 2025/07/28 15:33:52