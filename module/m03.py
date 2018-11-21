import m01 as m_1  #通过import 模块 as 别名  给导入的模块取别名
s2=m_1.Student()
s2.say()
m_1.sayHello()


#导入模块-4,有选择性的导入
#from module_name import func_name,class_name

from m01 import  Student,sayHello

stu=Student()
stu.say()
sayHello()


#导入模块的所有内容
# import module_name import *

from m01 import *
sayHello()
s3=Student("zhangsan",15)
s3.say()