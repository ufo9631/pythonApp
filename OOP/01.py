class Student():
    pass #一个空类，pass代表直接跳过

s1=Student() #创建一个对象

class PythonStudent():
   #用None给不确定的值赋值
   name=None
   age=18
   course="Python"
    #默认有一个self参数 #推荐函数末尾使用return语句
   # self 表示对象本身，谁调用指的就是谁，如果通过对象调用一个方法，那么该对象会走动传入当前方法的第一个参数，self不是关键字 可以是任何参数名
   def doHomework(self):
       self.name="yaona"
       self.age=17
       print("My name is {0}".format(self.name))
       print("My age is {}".format(self.age))
       print("I 在做作业")
       return None
   def sayAgain(): #无法使用实例访问，因为没绑定到实例上，可以用类名访问
        print(__class__.name)
        print(__class__.age)
        print("Hello ,nice to see you again")

zhangsan=PythonStudent()
zhangsan.doHomework()
#zhangsan.sayAgain()
PythonStudent.sayAgain() #
print(PythonStudent.__dict__)
#通过默认内置变量检测类和对象的成员
#对象检查所有成员
#dict前后各两个下划线
#obj.__dict__

#方法中有self形参的方法称为非绑定类的方法，可以通过对象访问，没有self的是绑定类的方法只能通过类访问
#使用类访问绑定类的方法时，如果类方法中需要访问当前类的成员，可以通过__class__成员名来访问

#关于self的案例
class A():
    name="liuying"
    age=18
    def __init__(self):
        self.name="aaaa"
        self.age=200
    def say(self):
        print(self.name)
        print(self.age)

class B():
    name="bbb"
    age=90
a=A()
#此时，系统会默认把a作为第一个参数传入参数
a.say()
#此时，self被a
A.say(a)

A.say(A)
#此时，传入的类实例B,因为B具有name和age属性，所以不会报错
A.say(B)
#以上代码，利用了鸭子模型



