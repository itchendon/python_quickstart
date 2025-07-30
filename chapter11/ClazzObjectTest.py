class Person(object):
    count = 0  # 类属性

    def __init__(self, name, age, address):  # 初始化函数，对实例属性进行修改
        self.name = name  # 实例属性
        self.age = age
        self.address = address
        Person.count += 1

    # 实例方法
    def display(self):
        print(self.name, self.age, self.address)

    # 类方法
    @classmethod
    def show(cls):
        print(cls.count)
    # 主要区分于是否和类有关，类方法是和类有关的，而静态方法是和类没多大的关系的才使用。
    @staticmethod
    def validParam(**keyword):
        if keyword.get('age') < 18:
            print("未成年人....")
            return False
        return True

# 创建对象
zhansan = Person('张三', 20, '广西壮族自治区');
# 修改对象属性
zhansan.address = '广西壮族自治区北海市广东路西六巷'
print(zhansan.name, zhansan.age, zhansan.address)
# 打印字典
print(zhansan.__dict__)  # {'name': '张三', 'age': 20, 'address': '广西壮族自治区北海市广东路西六巷'}
print(zhansan, type(zhansan))
print(isinstance(zhansan, Person))
print(isinstance(zhansan, object))
print("欢迎第%d个游客%s的到来" % (Person.count, zhansan.name))
zhansan.display()
Person.show()
info={'name':'zhangsan','age':17,}
print(Person.validParam(**info))


# 继承
class Student(Person):
    def __init__(self, name, age, address,stuno):
        super().__init__(name, age, address)
        self.stuno = stuno
    def display(self):
        super().display()
        print(self.stuno)
print("调用重写的方法-----------"*5)
stu = Student('李四',20,'广东省深圳市区','12345678')
stu.display()

print("受保护的变量和私有变量的声明-----------"*5)
class Machine(object):
    def __init__(self, id,engine,logo):
        self._id = id # 受保护的变量
        self.__engine = engine  # 私有变量
        self.__logo = logo
    #     受保护的方法
    def _modify(self, id):
        self._id=id
        self.__modifyEngine('turbos')
        print(self._id,self.__engine)
    # 私有方法
    def __modifyEngine(self,engine):
        self.__engine=engine
    #     使用装饰器对方法的名称属性化，调用方法就像调用属性一样即可，但是，原来的直接 对象.方法()的方式不可用了。
    @property
    def logo(self):
        print("使用装饰器方式进行调用")
        return self.__logo;
    # 名字要一样的。
    @logo.setter
    def logo(self,logo):
        self.__logo=logo


m = Machine("1435",'turbo','aa')
print(m._id)
# print(m.__engine) # 私有变量无法直接访问
m._modify('214324324')
print(m._id)
# 打印对象实例的所有方法
print(dir(m)) # ['_Machine__engine', '_Machine__modifyEngine', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', '_id', '_modify']
print(m.logo)   # aa
m.logo='bb'
print(m.logo) # bb