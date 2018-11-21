#常用模块
#calendar  日历
import calendar
#获取一年日历的字符串
#参数
#w=每个日期之间的间隔字符数
#l=每周所占用的行数
#c=每个月剪的间隔字符数
cal=calendar.calendar(2018)
print(cal)
print("*"*20)
cal=calendar.calendar(2018,l=0,c=11)
print(cal)

#isleap:判断某一年是否是闰年
print(calendar.isleap(2000))
#leapdays：获取指定年份之间闰年个数
print(calendar.leapdays(1998,2018))
print(help(calendar.leapdays))

#month()获取某个月的日历字符串
#格式：calendar.month(年，月)
#返回值：月日历的字符串
print(calendar.month(2018,11))

#monthrange() 获取一个月第一天是周几 还有月份一共有几天
#格式calendar.monthrange(年，月)
#返回值：元组（周几开始，总天数）
#注意：周默认0-6 表示周一到周天
print(calendar.monthrange(2018,11))

#monthcalendar()返回一个月每天的矩阵列表
#格式calendar.monthcalendar(年，月)
#返回值：二级矩阵
#注意：矩阵中没有天数用0表示
m=calendar.monthcalendar(2018,11)
print(type(m))
print(m)

#prcal：直接打印日历
calendar.prcal(2018)

#prmonth()直接打印整个月的日历
#格式calendar.prmonth(年，月)
#返回值：无
calendar.prmonth(2018,11)

#weekday()获取周几
#格式：calendar.weekday(年，月，日）
#返回值：周几对应的数字
w= calendar.weekday(2018,11,10)
print(w)