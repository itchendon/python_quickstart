def func():
    print("hello world")


# 函数调用
func()


def mySum(a, b):
    return a + b


print(mySum(1, 2))
len("111")


# 给形参设置默认值
def cal(a, b=2):
    return a ** b


print(cal(3))  # 9
print(cal(3, 4))  # 81


num = int('16',8)
print(num)


def showInfo(name,age=24,gender='男'):
    print("Name:",name)
    print("Age:",age)
    print("Gender:",gender)

showInfo('zhangsan',gender='男')
print("-----"*10 )
showInfo('zhangsan',gender='女')
print("-----"*10 )
# 可变参数
def myCal(a):
    ret = 0;
    for i in a:
        ret+=i
    return ret
# 此时只能传递列表参数，如果只给以穿数据子就无法识别
print(myCal([1,2,3,4]))
# TypeError: myCal() takes 1 positional argument but 4 were given
# print(myCal(1,2,3,4))
#  *参数名称 就是可变参数的形式。
def myCal2(*a):
    ret = 0;
    for i in a:
        ret+=i
    return ret
arr = [1,2,3,4]
# 传递可变参数要使用 * ,否则就是多个逗号隔开的参数。
print(myCal2(*arr))
print(myCal2(1,2,3,4))

# 传递字典
def showDict(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

d = {
    'name': 'zhangsan',
    'age': 24,
    'gender':'男'
}
# 传递字典要使用**
showDict(**d)




