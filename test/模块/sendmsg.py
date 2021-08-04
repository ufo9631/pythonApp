def test1():
    print("test1")

def test2():
    print("test2")


print(__name__)

# __name__  ,当前文件自己执行时打印出来的是 __main__
# __name__  ,在被其它文件导入时打印出来的是 导入的模块名称
if __name__=="__main__":
    test1()
    test2()