
#模块导入
#语法 improt module_name
# module_name.function_name
#module_name.class_name
#借助于importlib包可以实现以数字开头的模块名称
import importlib
import m01  #导入就是把模块的代码都粘贴过来了

tuling=importlib.import_module("01") #相当于导入了一个叫做01的模块并把导入模块赋值给tuling

stu=m01.Student("zhangsan",20)
stu.say()
m01.sayHello()


s1=tuling.Student()
s1.say()
tuling.sayHello()

