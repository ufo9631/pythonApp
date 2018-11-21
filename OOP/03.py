class A():
    pass
class B(A):
    pass
class C(B,A):
    pass
print(A.__mro__)
print(B.__mro__)

#单继承和多继承
#单继承：每个类只能继承一个类
#多继承，每个类允许继承多个

#单继承和多继承的优缺点
#单继承：传承有序逻辑清晰语法简单隐患少
#单继承缺点：功能不能无限扩展，只能在当前唯一的继承链中扩展

#多继承：类的功能扩展方便
#多继承缺点：继承关系混乱



#15.1多继承，子类可以直接拥有父类的属性和方法
class Fish():
    def __init__(self,name):
        self.name=name
    def swim(self):
        print("i am swimging....")
class Bird():
    def __init__(self,name):
        self.name=name
    def fly(self):
        print("I am flying....")

class Person():
    def __init__(self,name):
        self.name=name
    def work(self):
        print("working....")
class SuperMan(Person,Bird,Fish):
    def __init__(self,name):
        self.name=name

s=SuperMan("zhangsan")
s.fly()
s.swim()


#菱形继承、钻石继承问题
#多个子类继承自同一个父类，这些子类由被同一个类继承，于是继承关系图形成一个菱形图谱
#MRO
#关于多继承的MRO就是多继承中，用于保存继承顺序的一个列表
#python 本身采用C3算法来多继承的菱形继承进行计算的结果
#MRO列表的计算原则：子类永远在父类前面，如果多个父类，则根据继承语法中括号内类的书写书序存放，如果多个类继承了同一个父类，孙子类中只会选取继承语法括号内的第一个父类


#构造函数
class Person():
    def __init__(self):
        self.name="NoName"
        self.age=18
        self.address="StudentTwhomnsdf"
        print("In init Func")

p=Person()


#构造函数的调用顺序
#如果子类没有写构造函数，则自动向上查找，直到找到
class A():
    def __init__(self):
        print("A")
class B(A):
    def __init__(self):
        print("B")
class C(B):
    pass

#此时C没有构造函数
#如果没有，则向上按照MRO顺序查找父类的构造函数
c=C()

#构造函数顺序-2
class A():
    def __init__(self):
        print("A")
class B(A):
    def __init__(self,name):
        print("B")
        print(name)
class C(B):
    pass

c=C("哈哈")


#构造函数顺序-3
class A():
    def __init__(self):
        print("A")
class B(A):
    def __init__(self,name):
        print("B")
        print(name)
class C(B):
    #c想扩展B的构造函数
    #即调用B的构造函数后再添加一些功能
    #由两种方法实现
    #第一种是通过父类名调用
   ''' def __init__(self,name):
        B.__init__(self,name)
        print("这是C中附加的功能")
    '''
    #第二种是通过super调用
   def __init__(self,name):
        super(C,self).__init__(name)
   pass

c=C("我是C")