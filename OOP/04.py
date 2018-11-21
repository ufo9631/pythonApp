#多态，就是同一个对象在不同情况下有不同的状态出现
#在python多态不是语法，是一种设计思想
#多态性，一种调用方式，不同的执行结果
#多态，同一事物的多种形态，动物分为人类，狗类，猪类

#Mixin设计模式
#主要采用多继承方式对类的功能进行扩展

#类相关函数
#issubclass:检测一个类是否是另一个类的子类
class A():
    name="NoName"
    pass
class B(A):
    pass
class C():
    pass

print(issubclass(B,A))
#isinstance:检测一个对象是否是一个类的子类
a=A()
print(isinstance(a,A))

#hasattr:检测一个对象是否有xxx成员
print(hasattr(a,"name"))

#getattr:get attribute
#setattr:set attribute
#delattr:delete attribute
#dir：获取对象成员列表
help(setattr)
print(dir(a))
print(dir(A))
