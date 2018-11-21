#time模块
#时间戳：指的是1970年1月1日0时0分0秒到现在经历的秒数
import  time
#时间模块的属性
#timezone:当前时区和UTC时间相差的秒数，在没有夏令时的情况下的间隔 ,东八区的是-28800
print(time.timezone)
#altzone::当前时区和UTC时间相差的秒数，在有夏令时的情况下的间隔
print(time.altzone)

#daylight 测试当前是否有夏令时时间状态 0表示是
print(time.daylight)

#得到时间戳
print(time.time())
#取得当前时间
t=time.localtime()
print(t)
#可以通过点号操作符得到相应的属性元素的内容
print(t.tm_hour)

#asctime()返回元组的正常字符串化的时间格式
#格式：time.asctime()时间元组
#返回值：字符串 Sun Nov 18 10:01:14 2018
tt=time.asctime(t)
print(tt)

#ctimeL:获取字符串化的当前时间
t=time.ctime()
print(t)

#mktime()使用时间元组获取对应的时间戳
#格式：time.mktime(时间元组)
#返回值：浮点数时间戳
lt=time.localtime()
ts=time.mktime(lt)
print(ts)

#clock:获取cpu时间

#sleep:使程序进入睡眠，n后继续
for i in range(1,10):
    print(i)
    #time.sleep(1) #程序会进入睡眠

#strftime:将时间元组转化为自定义的字符串格式
t=time.localtime()
ft=time.strftime('%Y{y}%m{m}%d{d} %H{h}%M{f}%S{s}').format(y='年',m='月',d='日',h='时',f='分',s='秒')
print(ft)


