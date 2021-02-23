class Demo:

    _c1 = 'demo1'  # protected类型 ,保护属性
    __c2 = 'demo2'  # private类型 ，私有属性
    __c3__ = 'demo3'  # 定义特殊方法，一般是系统定义名字，如__init__()

    number = 0

    def __init__(self):
        self.a = 1
        self.b = 2

        Demo.number += 1
        print('class:', Demo.number)

    def func(self, arg):
        print(arg)

    @property  # 将一个方法转为属性，访问不需加(),代码更简洁,只读属性
    def computed(self):
        return self.a+self.b

    @computed.setter  # 设置setter方法
    def computed(self, arg1):
        self.b = arg1


list1 = []
for i in range(5):
    list1.append(Demo())

demo1 = Demo()
print(demo1._c1)
print(demo1._Demo__c2)  # 通过 实例名._类名__xxx 访问

print(demo1.computed)  # 3

demo1.computed = 3
print(demo1.computed)


#------ 继承 ------

class Demoo(Demo):
    def __init__(self):
        print('Demoo extend Demo')
        super().__init__() #调用基类的__init__()方法

    def func(self):
        print('demoo')

demoo1 = Demoo()
demoo1.func()