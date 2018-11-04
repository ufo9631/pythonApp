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