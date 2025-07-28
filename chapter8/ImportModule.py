from modules import MyModule

import random
a = [1,2,3]
MyModule.showInfo(*a)
print(random.randint(1,100))

print("0000000000000"*5)

list1 = [1,3,5,7,8,6,9,2,4]
print(list1[random.randint(0,len(list1)-1)])
print("0000000000000"*5)

for v in range(len(list1)):
    print(random.choice(list1))
print("0000000000000"*5)

print(ord("A"),ord("Z"))

a=[]
for v in range(20):
    s='';
    for j in range(5):
        t=random.randint(65,90)
        s+=chr(t)
    a.append(s)
print(a)

print("0000000000000"*5)
list2=[1,2,3,4,5,6,7,8,9]
# 打乱列表顺序
random.shuffle(list2)
print(list2)




