#一个模块可以包含python代码文件，后缀名是.py，模块就是个python文件
#模块可以增加代码重复利用的方式
#当做命名空间使用，避免命名冲突


#如何定义模块，
#模块就是一个普通的文件，所以任何代码可以直接书写
#根据模块规范，最好在模块中编写以下内容
#函数（单一功能）
#类（相似功能的组合，或是类似业务模块）
#测试代码



#如何使用模块
#模块直接导入
class Student():
    def __init__(self,name="NoName",age=18):
        self.name=name
        self.age=age
    def say(self):
        print("My name is {0}".format(self.name))
def sayHello():
    print("Hi,欢迎光临")

 #当这个文件被自己调用的时候执行，当被其它文件导入时，不执行该方法
 #判断语句建议作为程序的入口
if __name__=='__main__':
    print("测试........")

