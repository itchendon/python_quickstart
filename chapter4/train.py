year=2024
if year%4==0 and year%100!=0 or year%400==0:
    print("%s是闰年"%(year))
else:
    print("非闰年")