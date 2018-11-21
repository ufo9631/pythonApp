#属性案例,属性的定义，描述类成员，可以在类中对类成员进行相关操作而创建的一种方式
#属性的操作 get,set,delete,如果想使用成员描述符有三种方法，
#1. 使用类实现
#2.使用属性修饰符
#3.使用property函数
#property(fget,fset,fdel,doc)

#创建Student类，描述学生类
#学生具有Student.name属性
#但name格式不确定
class Student():
    '''
    这是一个描述文档
    '''
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def intro(self):
        print("hi my name is {0}".format(self.name))
    def fget(self):
        return  self._name
    def fset(self,name):
        #以大写形式保存
        self._name=name.upper()
    def fdel(self):
        self._name="NoName"
    def addrIntro(self):
        print(self.addr)
    name=property(fget,fset,fdel,"对name进行操作")
    addr=property(fget,fset,fdel,"对name进行操作")
    def __call__(self, *args, **kwargs):
        print("__Call__ args={0},kwargs={1}".format(args,kwargs))
    def __str__(self):
        return "我被调用了"
s1=Student("liu xing",19)
s1.addr="sdflsdjflsj"
s1.addrIntro()
s1('sdfsdf','哈哈哈',19)#实例当函数调用需要定义__call__方法
print(s1) #实例被当字符串调用时，自动触发__str__方法
s2=Student("zhagnsan",25)
s1.intro()
s2.intro()

#类的内置属性
#__dic__：以字典的的方式显示类的成员组成
#__doc__:获取类的文档信息
#__name__:获取类的名称，如果在模块使用，获取模块的名称
#__bases__:获取某个类的所有父类，以元组的方式显示

print(Student.__dict__)
print(Student.__doc__)
print(Student.__name__)
print(Student.__bases__)

#类的常用魔术方法
#魔术方法就是不需要人为调用，基本就是在特定时刻触发
#魔术方法的特征，方法名的前后各两个下划线包裹
#__init__：构造函数
#__new__:对象实例化方法这个的调用比__init__早，此函数比较特殊，一般不需要使用
#__call__:对象当函数使用的时候触发
#__str__:当对象当做字符串调用时触发
#__repr__:返回字符串跟__str__具体区别，查百度

#描述符相关
#__set__
#__get__
#__delete__

#属性相关描述符
#__getattr__:访问一个不存在的属性触发
#__setattr__：对成员属性进行设置时触发，作用：进行属性设置的时候进行验证或修改，注意，在该方法不能对属性直接进行操作，否则会死循环

class A():
    name="Noname"
    age=18
    def __init__(self):
        pass
    def __getattr__(self, item): #未找到属性自动调用
        print("没找到")
    def __setattr__(self, instance, value):
        print("设置属性：{0}".format(instance))
        pass
a=A()
a.name="zhangsan"
print(a.name)
print(a.addr)


#运算符分类魔术方法
#__gt__:进行大于判断时候触发
class Student():
    def __init__(self,name):
        self._name=name
    def __gt__(self, other):
        print("haha{0}会比{1}大吗".format(self,other))
        return self._name>other._name
stu1=Student("one")
stu2=Student("two")
print(stu1>stu2)

#类和对象的三种方法
#实例方法，需要实例化对象才使用的方法
#静态方法，不需要实例化，通过类直接访问
#类方法，不需要实例化
class Person():
    #实例方法
    def eat(self):
        print(self)
        print("Eating")
    #类方法,一般命名为cls，区别于self
    @classmethod
    def play(cls):
        print(cls)
        print("playing")
    #静态方法
    #不需要用第一个参数表示自身或类
    @staticmethod
    def say():
        print("Saying")
p=Person()
#实例方法
p.eat()
#类方法
Person.play()
p.play() #也是当做类调用

Person.say()