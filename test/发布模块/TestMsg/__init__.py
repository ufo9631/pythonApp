#在 TestMsg 文件夹下 创建__init__.py文件，那么python解析器就会认为TestMsg是一个包 文件名必须叫做__init__.py
__all__=["sendmsg"]   #在一个包里写__all__表示要导出的模块
print("hahhah1")
#import sendmsg #python2可以在__init__ 可以这样用 python3不能用

from . import  sendmsg  #.表示当前路径