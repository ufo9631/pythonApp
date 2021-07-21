#变量
#全局变量（global）:在函数外部定义
#局部变量（local）：在函数内部定义

#提升局部变量为全局变量
def fun():
    global bl
    b1=100
    print(bl)
    print("I am in fun")
    b2=99
    print(b2)

#print(b1)

#globals,locals函数
#可以通过globals和locals出局部变量和全局变量
a=1
b=2
def fun(c,d):
    e=111
    print("Locals={}".format(locals()))
    print("Globals={}".format(globals()))

fun(100,200)

#eval()函数 把一个字符串当成一个表达式来执行，返回表达式执行的结果
x=100
y=200
z=eval("x+y")
print(z)

#exec()函数，跟eval()功能相似，但是不返回结果
x=100
y=200
z=exec("x+y")
print(z)

#递归函数
#函数调用自己
#优点：简洁，理解容易
#缺点：对递归深度有限制，消耗资源大
#python对递归深度有限制，超过限制报错

#递归调用深度限制代码
x=0
def fun():
    global x
    x+=1
    print(x)
    fun()
#fun()

#内置数据结构（变量类型）
#list,set,dict,tuple
#list(列表) 一组有顺序的数据的组合
l1=[]
print(type(l1))
l2=[100]
print(type(l2),l2)
l3=list()
print(type(l3),l3)
#使用下标（索引）访问列表
l=[3,4,5,9,6,1,3]
print(l[0])
#分片操作，下标值可以为空，如果不写，左边下标值默认为0，右边下标值为最大数加一，即表示取到最后一个数据
print(l[1:3])  #[:] 分片的范围左开右闭
print(l[-2:-1])
print(l[:])
#分片可以控制增长幅度，默认增长幅度为1
print(l[1:6:2]) ## 第二个冒号表示补偿长度  从2到-1 然后隔一个取一个
#下标可以朝出范围，超出后不在考虑多余下标内容
#如果分片一定左边值比右边大，则幅度增长参数需要使用负数
print(l[-2:-4:-1])  #相当于一个逆序的效果
#分片操作是生成一个新的list
#内置函数id，负责显示一个变量或数据的唯一确定编号
#id函数举例
a=100
b=200
print(id(a))
print(id(b))

#list 删除
del l[2]
print(l)
#列表相加
a=[1,2,3,4,5]
b=[6,7,8,9,10]
print(a+b)
#使用乘号操作列表
a=[1,2,3]
b=a*3
print(b)
#成员资格运算，判断一个元素是否在list里边
a=[1,2,3,4,5]
b=8
c=b in a # c是一个布尔值
print(c)
print(b not in a)
#列表的遍历for,while
a=[1,2,3,4,5]
for i in a: # in 后面的变量要求是可以可迭代的内容
    print(i)
b=["I love chenweichao"]
for i in b:
    print(i)
#一般不用while list
a=[1,2,3,4,5]
length=len(a)
indx=0
while indx<length:
    print(a[indx])
    indx+=1
#双层列表循环
a=[["one",1],["two",2],["three",3]]
for k,v in a:
    print(k,"-",v)

#列表内涵：list content
#for创建
a=['a','b','c']
#用list a创建一个list b
b=[i for i in a]
print(b)
#过滤原来list中的内容放入新列表
a=[x for x in range(1,35)]
b=[m for m in a if m%2==0]
print(b)
#列表生成可以嵌套
a=[i for i in range(1,10)]
print(a)
b =[i for i in range(100,1000) if i%100==0]
print(b)
c=[m+n for m in a for n in b]
print(c)

for m in a:
    for n in b:
        print(m+n,end=" ")

print()
#列表常用函数
#len:列表长度
a=[x for x in range(1,100)]
print(len(a))
#max 求列表最大值
#min 求列表最小值
print(max(a))
b=['man','film','python']
print(max(b))
#list 函数将格式数据转换成list
a=[1,2,3]
print(list(a))
s="I am chenweichao"
print(list(s))


#传值和传地址的区别
#对于简单的数值，采用传值的操作，即函数内对参数的操作不影响外面的变量
#对于复杂变量，采用传地址操作，此时函数内的参数和外部变量都是同一份，任何地方对此内容更改都影响变量

#关于列表的函数
l=['a','b',"c",45,766,5+7]

a=[i for i in range(1,5)]
print(a)
a.append(100) #在末尾插入
print(a)
a.insert(3,666)  #插入的是index的前面
print(a)

#删除
# del删除
#pop ,从对位拿出一个元素，即把最后一个元素取出来
last_ele=a.pop() #拿出最后一个元素
print(last_ele)
#remove:在列表中删除指定的值,要删除的值必须是存在的，否则报错
a.remove(666)
print(a)

#clear:清空
a.clear()
print(a)

#reverse:翻转
a=[1,2,3,4,5,6]
a.reverse()
print(a)
#extend:扩展列表，把两个列表，把一个直接拼接到后一个上
a=[1,2,3,4,5,6]
b=[6,7,8,9,10]
a.extend(b)
print(a)

#count:查找列表中指定值或元素的个数
a_len=a.count(8)
print(a_len)
#copy:拷贝，浅拷贝
#列表类型变量赋值示例
a=[1,2,3,4,5]
b=a.copy()
print(b)
print(id(a))
print(id(b))
#深拷贝跟浅拷贝的区别,对于多层嵌套的列表  浅拷贝只拷贝了一层，深拷贝需要使用特定工具
a=[1,2,3,[10,20,30]]
b=a.copy()

#元组-tuple,元组可以看成是一个不可更改的list
t=()
print(type(t))
#创建一个只有一个值的元组
t=(1,)
print(type(t))
print(t)

t=1,
print(type(t))

#创建多个值的元组
t=(1,2,3,4)
t1=1,2,3,4,5
print(type(t))
print(type(t1))

l=[1,2,3,4,5]
t=tuple(l)
print(type(t))
print(t)

#元组的特定
#是序列表有序
#元组数据可以访问，不能修改
#元素数据可以是任意类型
#总之，list所有特定，除了可修改外，元组都具有

#索引操作
t=(1,2,3,4,5)
print(t[4])

t=(1,2,3,4,5,6)
t1=t[1::2]
print(t1)

#切片可以超标
t2=t[2:100]
print(t2)

#tuple 相加
t=(1,2,3)
t2=(5,6,7)
t1+=t2
print(t1)

#成员检测
t=(1,2,3,4)
if 2 in t:
    print("Yes")
else:
    print("No")

#元组遍历，一般采用for
#单层元组遍历
t=(1,2,3,4,"i","a","b")
for i in t:
    print(i,end=" ")

#双层元组遍历
t=((1,2,3),(2,3,4),('a','b','c'))
for i in t:
    print(i)

for k,m ,n in t:
    print(k,'---',m,'-----',n)

#关于元组的函数
#len:获取元组的长度
t=(1,2,3,4,5)
print(len(t))
#max ,min 最大最小值,如果列表或元组有多个最大或最小值，则实际打印出哪个
print(max(t))
print(min(t))

#tuple:转化或创建元组
l=[1,2,3,4,5]
t=tuple(l)
print(t)

t=tuple()
print(t)

#元组的函数
# 基本跟list通用
#count: 计算指定数据出现的次数
t=(1,22,2,3,4,4,5,6,6)
print(t.count(3))
#index:找出指定的元素在元组中的索引位置
print(t.index(4))

#元组变量交换法
#变量交换值
a=1
b=3
a,b=b,a
print(a)
print(b)

#集合Set,集合是数据概念
#一堆确定的无序的唯一的数据，集合中每个数据成为一个元素
#集合的定义
s=set()
print(type(s))

s={1,2,3,4,5}
print(type(s)) #大括号定义有值的表示set
print(s)

#如果只是用大括号定义，则定义的是一个dict类型
d={}
print(type(d))


#集合的特征
#集合内数据无序，即无法使用索引和分片
#集合内部数据元素具有唯一性，可以用来排除重复数据
#集合的数据包括可哈希的数据
#集合序列操作，成员检测
s={2,3,4,'a','b','sdfsdfsdfd'}
print(s)
if 2 in s:
    print("Yes")

#集合遍历操作
s={2,3,4,'a','b','sdfsdfsdfd'}
for i in s:
    print(i,end=" ")

print()
#带有元组的集合遍历
s={(1,2,3),('a','b','c'),(4,6,5)}  #不能放集合，集合是不可哈希
for k in s:
    print(k)
for k,m ,n in s:
    print(k,'---',m,'----',n)

#集合的内涵
#普通的集合内涵,以下集合会自动过滤掉重复的
s={23,1,3,4,5,6,33,7,1,2,3,4,5}
print(s)
ss={i for i in s}
print(ss)

#带条件的集合内涵
sss={i for i in s if i%2==0}
print(sss)

#多循环的集合内涵
s1={1,2,3,4}
s2={'a','b','c'}
s={m*n for m in s1 for n in s2}
print(s)

#集合函数、关于集合的函数
#len,max,min
s={1,2,34,54,34,65,76}
print(len(s))
print(max(s))
print(min(s))

# set 生成一个集合
l=[1,2,3,4,5,6]
s=set(l)
print(s)

#add 向集合内添加元素
s={1}
s.add(234)
print(s)

#clear
s={1}
print(s.clear())

#copy 拷贝
#remove 移除指定的值，如果删除的值不存在 报错
#discard:移除集合指定的值，跟remove一样，但是值不存在的话，不报错
s={12,3,2,4,5}
s.remove(4)
print(s)
s.discard(12)
s.discard(1000)

#pop 随机移除一个元素
s={1,2,3,4,5,6}
d=s.pop()
print(d)
print(s)
#集合函数
#intersection:交集
#difference:差集
#union:并集
#issubset检查一个集合是否为另一个子集
#issuperset:检查一个集合是否为另一个超集
s1={1,2,3,4,5}
s2={3,4,5,6,7}
s_1=s1.intersection(s2)
print(s_1)
s_2=s1.difference(s2)
print(s_2)
s_3=s1.issubset(s2)
print(s_3)

#集合的数学操作
s1={1,2,3,4,5}
s2={3,4,5,6,7}
s_1=s1-s2
print(s_1)
s_2=s1+s2
print(s_2)
#冰冻集合，冰冻和就是不可以进行任何修改的集合,frozenset是一种特殊集合
s=frozenset()
print(type(s))
print(s)

