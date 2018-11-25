#函数作为返回值返回
def myF2():
    def myF3():
        print("In myF3")
        return 3
    return myF3

f3=myF2()
print(type(f3))
print(f3)
f3()

#返回函数稍微复杂的例子
#args:参数列表

def myF4(*args):
    def myF5():
        rst=0
        for n in args:
            rst+=n
        return rst
    return myF5
f5=myF4(1,23,5,6,7,8)
print(f5())

#闭包 （closure）
#当一个函数在内部定义函数，并且内部的函数应用的函数应用外部函数的参数或者局部变量，当内部函数被当做返回的时候，相关参数和变量保存在返回的函数中，这种结果，叫做闭包



#闭包常见的坑
def count():
    #定义列表,列表里存放的是定义的函数
    fs=[]
    for i in range(1,4):
        #定义了一个函数f
        #f是一个闭包结构
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3=count()
print(f1())
print(f2())
print(f3())
#出现的问题
#造成上述状况的原因是，返回函数引用了变量i,i并非立即执行，而是等到三个函数都返回的时候才统一使用，此时i已经变成了3，最终调用的结果，都返回的是3*3
#此问题描述：返回闭包时，返回函数不能引用任何循环变量
#解决方案：再创建一个函数，用该函数的参数绑定循环变量的当前值，无论该循环变量以后如何改变，已经绑定的函数参数值不再改变

def count2():
    def f(j):
        def g():
            return j*j
        return g()
    fs=[]
    for i in range(1,4):
        fs.append(f(i))
    return fs
f1,f2,f3=count2()
print(f1())
print(f2())
print(f3())