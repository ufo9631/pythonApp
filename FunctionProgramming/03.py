#装饰器
def hello():
    print("hello world")
hello()
f=hello
f()

#对hello功能进行扩展，每次打印hello之前打印当前系统时间
#而这个功能又不能改动现有代码
#装饰器

#装饰器
#在不改动函数代码的基础上无限制扩展函数功能的一种机制，本质上讲，装饰器是一个返回函数的高阶函数
#装饰器的使用：使用@语法，即在每次要扩展的函数定义前使用#+函数名
import time
#高阶函数，以函数作为参数
def printTime(f):
    def wrapper(*args,**kwargs):
        print("Time:",time.ctime())
        return f(*args,**kwargs)
    return wrapper
#上面定义了装饰器，使用的时候需要用到@，此符号是python的语法糖
@printTime
def hello():
    print("Hello world")
hello()

#装饰器的好处是，一定义则可以装饰任何函数
#一旦被其装饰，则把装饰的功能直接添加到定义函数的功能上
@printTime
def hello2():
    print("今天高高兴兴")
    print("hahahhahahha")
hello2()


#手动执行装饰器
def hello3():
    print("我是手动执行")
hello3()

hello3=printTime(hello3)
hello3()

f=printTime(hello3)
f()


#偏函数
#把字符串转为十进制数字
print(int("12345"))
print(int("12345",8))

#偏函数
#参数固定的函数，相当于一个由特定参数的函数体
#functools.partial的作用是，把一个函数某些函数固定，返回一个新函数
import functools
int16=functools.partial(int,base=16)
print(int16("12345"))
