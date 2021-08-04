try:
    open("xxxx.txt")
    print(num)
    print("----1---------")
except (NameError,FileNotFoundError): #捕获多个异常
    print("如果捕获到异常后做的处理")
except FileNotFoundError:
    print("文件找不到....")
except Exception as ret:#异常信息会存放到ret里
    print("如果用了Exception，那么意味着上面的except没有捕获到异常，这个except一定会捕获到")
    print(ret)
else:
    print("没有异常才会执行")    
finally:
    print("------finally-------无论有没有异常最后都会执行")

print("----2---------")