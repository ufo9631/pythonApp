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

