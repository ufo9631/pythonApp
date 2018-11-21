#异常
#python 异常是一个类，可以处理和使用
# try:
# except 异常类型1:
#   解决方案1：用于尝试在此处处理异常问题
#except （异常类型2，异常类型3）：
#   解决方案2：用于尝试在此处处理异常问题
#except：
#   解决所有的异常
#else:
#   如果没有出现任何异常，江蕙执行此代码
#finally:
#   不管没有异常都会执行
try:
    num=int(input("input number:"))
    rsg=100/num
    print("计算结果：{0}".format(rsg))
#以下语句是捕获ZeroDivisionError异常并实例化e
except ZeroDivisionError as e:
    print("chucuo")
    print(e)
except: #except Exception as e:
    print("出错")
    exit() #exit是退出程序的意思


#用户手动引发异常
#raise 关键字来引发异常 raise 后面跟异常类

try:
    print("hahah ")
    raise ValueError  #手动引发异常
    print("还没完")
except Exception as e:
    print("有异常")
finally:
    print("我肯定会被执行")


#raise案例2
#自己定义异常类
#需要注意：自定义异常必须是系统异常的子类
class DanaError(ValueError):
    pass

try:
    print("hahah ")
    raise DanaError  #手动引发异常
    print("还没完")
except DanaError as e:
    print("dana异常类")
except Exception as e:
    print("有异常")
finally:
    print("我肯定会被执行")


#else语句案例
try:
    num = int(input("input number:"))
    rsg = 100 / num
    print("计算结果：{0}".format(rsg))
except Exception as e:
    print("Execption")
else:
    print("No Exception")
finally:
    print("我一定会被执行")

#关于自定义异常
#只要是raise异常，则推荐自定义异常
#在自定义异常的时候，一般包含以下内容
#自定义发生异常的代码
#自定义异常发生后的问题提示
#自定义异常的行数
#最终的目的是，一旦发生异常，方便程序员快速定位异常错误

