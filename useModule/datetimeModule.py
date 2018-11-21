#datetime模块
#datetime提供日期和时间的运算和表示
import  datetime
#datetime常见属性
#datetime.date ：一个理想和的日期，提供year,month,day属性
dt=datetime.date(2018,11,18)
print(dt)
print(dt.day)
print(dt.year)
print(dt.month)
#datetime.time:提供一个理想和的时间，提供hour,minute,sec,microsec等内置属性
#datetime.datetime:提供日期跟时间的组合
#datetime.timedelta:提供时间差，时间长度

#datetime.datetime
from datetime import  datetime
import  time
#常用类方法
#today
#now
#utcnow
#fromtimestamp:从时间戳返回本地时间
dt=datetime(2018,11,18)
print(dt.today())
print(dt.now())

print(dt.fromtimestamp(time.time()))

#datetime.timedelta 表示一个时间间隔
from datetime import datetime,timedelta
t1=datetime.now()
print(t1)
ft=time.strftime('%Y{y}%m{m}%d{d} %H{h}%M{f}%S{s}').format(y='年',m='月',d='日',h='时',f='分',s='秒')


import timeit

#timet 时间测量工具
#测量程序运行时间间隔实验
def p():
    time.sleep(3.6)
t1=time.time()
p()
print(time.time()-t1)

#生成列表两种方法的比较

c='''
sum=[]
for i in range(1000):
    sum.append(i)
'''
#利用timeit代码，执行100000次，查看运行时间
t=timeit.timeit(stmt="[i for i in range(1000)]",number=100000)

#测量代码c执行100000次运行结果
t2=timeit.timeit(stmt=c,number=100000)
print(t)
print(t2)

#timeit 可以执行一个函数，来测量一个函数的执行时间
def doIt():
    num=3
    for i in range(num):
        print("repeat for {0}".format(num))

t=timeit.timeit(stmt=doIt,number=10)
print(t) #

s='''
def doIt(num):    
    for i in range(num):
        print("repeat for {0}".format(num))
'''
#执行doIt(num)
#setup负责把环境变量准备好
t=timeit.timeit("doIt(num)",setup=s+"num=3",number=10)

#datetime.datetime模块
#提供比较好用的时间而已
from datetime import  datetime as dt
print(dt.now())