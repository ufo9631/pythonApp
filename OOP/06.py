#抽象类
#抽象方法：没有具体的实现
#抽象类的使用模块abc
#包含抽象方法的类叫做抽象类，通常叫做abc
class Animel():
    def sayHello(self):
        pass

class Dog(Animel):
    def sayHello(self):
        print("闻一下对方")

class Person(Animel):
    def sayHello(self):
        print("hello ")

d=Dog()
d.sayHello()
p=Person()
p.sayHello()

import  abc
#声明一个类并且制定当前类的元类为抽象类
#抽象类的使用：抽象类可以包含普通方法（有方法体）
#抽象类中可以有方法也可以有属性
#抽象类不允许直接实例化
#必须继承才可以使用，子类必须实现抽象类
#假定子类没有实现所有继承的抽象方法，则子类也不能实例化
#抽象类的主要作用是指定标准，以便开发的时候统一规范
class Human(metaclass=abc.ABCMeta):
    #定义抽象方法
    @abc.abstractmethod
    def somking(self):
        pass
    #定义类抽象方法
    @abc.abstractclassmethod
    def drink(cls):
        pass
    #定义静态抽象方法
    @abc.abstractstaticmethod
    def play():
        pass
    def sleep(self):
        print("睡觉")

#自定义类
#类其实是一个类定义和各种方法的自由组合

#自己组装一个类
class A():
    pass
def say(self):
    print("saying")

say(9)
#函数名当变量使用
A.say=say

a=A()
a.say()

#函数名当变量使用
def sayHello(name):
    print("{}你好，how are you".format(name))

l=sayHello
l("zhangsan")

#类组装例子-2
from types import MethodType
class A():
    pass
def say(self):
    print("Saying")

a=A()
a.say=MethodType(say,A)  #实例绑定方法需要使用 MethodType模块，第一个参数是方法，第二个参数指定绑定到哪个类上
a.say()

#可以定义类和函数，然后自己通过类直接赋值，可以借助于MethodType实现
#使用type造一个类
#先定义类应该有的成员函数
def say(self):
    print("自定义类Saying")
def talk(self):
    print("自定义类talking")
#用type创建一个类
A=type("AName",(object,),{"class_say":say,"class_talk":talk})  #类名称，父类，类成员
#实例化创建的类
a=A()
a.class_say()
a.class_talk()

#利用元类实现-  MetaClass
#元类是类
#被用来创造其它类的类

#元的写法是固定的，必须继承type
#元类一般命名以MetaClass结尾
class TulingMetaClass(type):
    #注意以下写法
    def __new__(cls, name,bases,attrs):
        #自己的业务代码
        print("haha 我是元类")
        attrs["id"]="00000"
        attrs["addr"]="厦门"
        return  type.__new__(cls, name,bases,attrs)

#元类定义完就可以使用，注意写法
class Teacher(object,metaclass=TulingMetaClass):
    pass
t=Teacher()
print(t.__dict__)
print(t.id)