#封装，继承，多态

#封装
#封装的三个级别，public,protected,private 不是关键字
#判别位置，对象内部，对象外部，子类中
#私有：在成员前面添加两个下划线即可
class Person():
    name="zhangsan" #公共成员
    __age=18 #age私有成员

p=Person()
print(p.name)
#Python的私有不是真的私有，是一种称为 name mangling的改名策略，可以使用对象._classname_attribute访问


#name mangling技术
print(Person.__dict__)
p._Person__age=19
print(p._Person__age)


#protected
#定义成员前面加一个下划线

#公开的，公共的public

##继承
#在python中，任何类都有一个共同的父类叫做object
class Person():
    name="NoName"
    age=0
    _petname="sec" #受保护的，子类可以用，但不能共用
    __score=0 #私有的
    def sleep(self):
        print("sleeping...")
    def work(self):
        print("make some money")
#父类写在括号里
#子类存在与父类相同的成员时优先使用子类的成员
#子类如果想扩充父类的方法，可以在定义新方法的同时访问父类成员来进行代码重用，可以使用【父类名.父类成员】的格式来调用父类成员，也可以使用【supper().父类成员】的格式来调用
class Teacher(Person):
    teacher_id="9527"
    def make_test(self):
        print("attention")

    def work(self):
        #扩充父类功能只需要调用相应的函数
        Person.work(self)
        #调用父类的另一种方法
        super().work()
        self.make_test()
    pass

t=Teacher()
print(t.name)
print(Teacher.name)
#受保护外部能访问，为啥这里可以访问
print(t._petname)

print(t.teacher_id)
t.make_test()
t.work()
#print(t.__score) #私有不能访问


#继承变量函数的查找顺序问题
#优先查找自己的变量
#没有则查找父类
#构造函数如果本类中没有定义，则自动查找调用父类构造函数
#如果本类有定义，则不再继承向上查找
#15.构造函数

class Dog():
    #__init__构造函数
    #每次实例化的的时候，第一个被调用
    #因为主要工作是进行初始化
    def __init__(self):
        print("i am init dog")
#实例化的时候，括号的参数需要跟构造函数的参数匹配
d=Dog()
print("*"*20)
#继承中的构造函数
class Animel():
    def __init__(self):
        print("Animel")
class PaxingAni(Animel):
    def __init__(self):
        print("Paxing dongwu")
class Dog(PaxingAni):
    def __init__(self):
        print("i am init dog")

#在子类中找到了构造函数，则不在查找父类的构造函数
kk=Dog()
print("*"*20)
class Cat(PaxingAni):
    pass
#此时自动调用父类的构造函数
c=Cat()
print("*"*20)
#继承中的构造函数-3
class Animel():
    def __init__(self):
        print("Animel")
class PaxingAni(Animel):
    def __init__(self,name):
        print("Paxing dongwu {0}".format(name))
class Dog(PaxingAni):
    def __init__(self):
        print("i am init dog")

d=Dog() #参数匹配不报错

class Cat(PaxingAni):
    pass

c=Cat('miaomiao') #此时会调用父类的构造函数，所以实例化的时候需要穿参数

#super,是不是关键字，而是一个类
#super的作用是获取MRO(MethodResolustionOtder)(MRO=方法解析列表） 列表中的第一个类
#super于父类直接没有任何实际性关系，但通过super可以调用到父类
#super使用两个方法，常见在构造函数调用父类的构造函数
