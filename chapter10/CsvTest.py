import csv
# with open("data.csv",mode='r+',encoding='utf-8') as f:
#     # 读取csv文件内容
#     cf = csv.reader(f)
#     # 读取csv文件头
#     head =  next(cf)
#     scores=[];
#     for row in cf:
#         print(row)
#         scores.append(int(row[2]));
#     print(sum(scores)/len(scores))

with open("data.csv", mode='a', encoding='utf-8') as f2:
   cf = csv.writer(f2)
   cf.writerow(['张三','语文',90])
   list2 = [['李四','语文',92],['李四','数学',96],['李四','英语',88]]
   cf.writerows(list2)