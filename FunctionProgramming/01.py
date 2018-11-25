#python语言的高级特性
#函数式编程
#基于lamb演算的一种编程方式
#程序中只有函数
#函数作为参数，同样可以作为返回值
#python函数式编程只是借鉴函数式编程的一些特点，可以理解成一半函数式编程一半是python

#lambda表达式(匿名函数)
#一个表达式，函数体相对简单
#不是一个代码块，仅仅是一个表达式
#可以有参数，多个参数用逗号隔开

#lambda表达式的用法
#1.以lambda开头
#2.紧跟一定的参数（有的话）
#3.参数后用冒号隔开，表达式和主体隔开
#4.只是一个表达式

#计算一个数字的100倍数
stm=lambda x:100*x
res=stm(89)
print(res)


stm2=lambda  x,y,z :x+y*10+z*100
print(stm2(4,5,6))


#高阶函数
#把函数作为参数使用的函数，叫做高阶函数

#函数名称就是一个变量
def funA():
    print("funA")
funB= funA
funB()

#函数名称就是变量
#funB和funA只是名称不一样而已
#既然函数名称是变量，则应该被当做参数传入另一个函数

#高阶函数举例
#funA是普通函数，返回一个传入数字的100倍数字
def funA(n):
    return n*100
#传入参数乘以300倍，利用高阶函数
def funB(n):
    return funA(n)*3

print(funB(9))


#写一个高阶函数
def funC(n,f):
    return  f(n)*3
print(funC(9,funA))

#系统高阶函数  map
#原意就是映射，即把集合或者列表的元素，每一个元素都按照一定规则进行操作，生成一个新的列表集合
#map函数是系统提供的具有映射功能的函数，返回是一个迭代的对象

#map举例，有一个列表，相对列表的每一个元素乘以10，并得到新的列表
l=[i for i in range(10)]
print(l)
l2=[]
for i in l:
    l2.append(i*10)
print(l2)

#利用map实现
def mulTen(n):
    return n*10
l3=map(mulTen,l)
#map类型是一个可迭代的结构，所以可以使用for遍历
for i in l3:
    print(i)

#以下列表生成式得到的结果为空why?
l4=[i for i in l3]
print(l4)


#reduce
#原意是归并，缩减
#把一个可迭代对象最后归并成一个结果
#对于作为参数的函数要求：必须有两个参数，必须有返回结果
#reduce需要导入functools包
#reduce([1,2,3,4,5])==f(f(f(f(1,2),3),4),5)


from functools import  reduce
#定义操作函数
def myAdd(x,y):
    return  x+y
rst=reduce(myAdd,[1,2,3,4,5,6]) #对列表[1,2,3,4,5,6]执行myadd的reduce操作
print(rst)


#fileter 函数
#过滤函数：对一组数据进行过滤，符合条件的数据会生成一个新的列表并返回
#跟map比较：
#相同：都对列表的每一个元素逐一进行操作
#不同：map会生成一个跟原来数据想对应的新队列
#filter不一定，只要符合条件的才会进入新的 数据集合
#filter函数怎么写：
#利用给定函数进行判断
#返回值一定是个bool值
#调用格式：filter(f,data) f是过滤函数，data是数据

#filter案例
def isEven(a):
    return  a%2==0

l=[1,2,3,4,5,5,6,7,8,10]
rst=filter(isEven,l)
print(rst)
for i in rst:
    print(i)

print([i for i in rst])

#高阶函数-排序
#把一个序列按照给定的算法进行排序
#key:在排序前对每一个元素进行key函数运算，可以理解成按照key函数定义的逻辑进行排序
a=[123,443,54,64,4,5,234,567,867]
al=sorted(a,reverse=True) #reverse=True倒序
print(al)

#排序案例2
a=[-45,-8,45,1,3,98,45,68,99]
#按照绝对值进行排序
#abs是绝对值的函数
al=sorted(a,key=abs,reverse=True)
print(al)

astr=['sdf','wE','eD','sdfwer']
str1=sorted(astr)
print(str1)
str2=sorted(astr,key=str.lower)
print(str2)

#返回函数
#函数可以返回具体的值
#也可以返回一个函数作为结果
def myF(a):
    print("In MyF")
    return None
a=myF(8)
print(a)


