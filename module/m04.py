#模块的搜索路径和存储
#模块的搜索路径：加载模块的时候，系统会在哪些地方寻找此模块
#系统默认的模块搜索路径
# import sys
#sys.path 可以获取路径列表
import  sys
print(sys.path)
for p in sys.path:
    print(p)
#添加搜索路径
sys.path.append("I://python") #添加搜索路径

#模块加载顺序
#搜索内存中已经加载好的模块
#搜索python的内置模块
#搜索sys.path路径


#包
#包是一种组织管理代码的方式，包里面放的是模块
#用于将模块包含在一起的文件夹就是包
#自定义包的结构
#包至少需要包含一个__init__.py文件



#包的导入操作
#import package_name
#直接导入一个包，可以使用__init__.py中的内容
#直接使用方式：
#package_name.func_name
#package_name.class_name.func_name()


#import package_name as p  #此种方法默认是对__init__.py内容的导入


#import package.module #导入包里的某个模块
  #使用方法 package.module.func_name
  # package.module.class.fun()
  #package.module.class.var

#import package.module as pm #取别名


# from ... import 导入
  # from package import module，module1,module2....
  #此种方法导入不执行 __init__的内容


# from package import*
  #导入当前包__init__文件所有的函数和类
  #使用方法
  #func_name()
  #class_name.func_name()
  #class_name.var

#from package.module import *
 #导入包中指定的模块的所有内容
 #使用方法
     #func_name()
     #class_name.func_name（）

#在开发环境中经常会用到其它模块，可以在当前包中直接导入其它模块的内容
# import 完整的包或模块的路径


#例子（08.py）
# __all__的用法，在使用from package import * 的时候，*可以导入的内容
#__init__.py 如果文件为空，或者没有，__all__ 那么直可以把__init__中的内容导入
#__init__如果设置了__all__的值，那么则按照__all__指定的子包或者模块进行导入，如此则不会载入__init__的内容

#命名空间
#用于区分不同位置不同功能但相同名称的函数或者变量的一个特定前缀
#防止命名冲突 
