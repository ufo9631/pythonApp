color=['red','yellow','blue','gree']
for green in color:
    print(green)
    if color=='green':
        print("Green")

#LOG
#logging 模块提供模块级别的函数记录日志
#包括四大组件
#1.日志概念
#日志级别（level）
#IO操作=》不要频繁操作

# 2 Loggin模块
# 日志级别
  # 日志级别可以自己定义
  #DEBUG
  #INFO
  #WARNING
  #ERROR
  #CRITICAL
# 初始化/写日志实例需要指定级别
#使用方式直接使用 logging(封装了其它组件)
#loggin四大组件直接定制

# 2.1 loggin模块级别的日志
#使用以下几个函数
'''
logging.debug(msg,*args,**kwargs) 创建一条严重级别为DEBUG的日志记录
logging.info(msg,*args,**kwargs)
logging.warning(msg,*args,**kwargs)
logging.error(msg,*args,**kwargs)
logging.critical(msg,*args,**kwargs)
logging.log(level,*args,**kwargs) 创建一条严重级别为level的日志记录
logging.basicConfig(**kwargs)  对root logger进行一次性配置，只在第一次调用的时候起作用
'''


#logging.basicConfig(**kwargs)  对root logger进行一次性配置，只在第一次调用的时候起作用
# 不配置logger则使用默认值
    # 输出：sys.stderr
    # 级别WARNING
    #格式 level:log_name:content

import  logging
LOG_FORMAT="%(asctime)s=======%(levelname)s++++++++++%(message)s"
logging.basicConfig(filename="log_debug.log", level=logging.DEBUG,format=LOG_FORMAT)


logging.debug("this is a debug log")
logging.info("this is a info log")
logging.warning("this is a warning log")
logging.error("this is a error log")
logging.critical("this is a critical log")

logging.log(logging.DEBUG,"this is a debug log")