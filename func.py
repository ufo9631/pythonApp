def hello(person):
    print("{0},你肿么了".format(person))
    print("Sir,吔屎啊你")
    return 'say hello'
p="zhangsan"
hello(p)
hello(person=p)
res=hello(person="xuexiang")
print(res)


## 收集参数  穿参的时候可以不传
#把没有位置，不能和定义时的参数位置对应的参数，放入一个特定的数据结构中
def func(*args):
   print(type(args)) #type 检测变量类型
   #按照list方式访问args传入的参数
   for i in args:
       print(i,end="") #end输入结束符  默认是换行

func(1,2,3,4,5)



#收集参数之关键字收集参数
#把关键字参数按字典格式传入收集参数
def fun(**kwargs):
    #kwargs 一般是约定俗称
    #调用的时候，把多余的关键字参数放入kwargs
    print(type(kwargs))
    print(kwargs["name"])
    for i in kwargs:
        print(i,end="")
    for k,v in kwargs.items():
        print(k,'****',v)


fun(name="zhangsan",age=18,addr="厦门",lover="lisi",work="tearcher")


#收集参数混合调用的顺序问题
#收集参数，关键字参数，普通参数可以混合使用
#使用规则就是，普通参数和关键字参数优先
#定义的时候一般找普通参数，关键字参数，收集参数tuple,收集参数dic
def fun(name,age,hobby='没有',*args,**kwargs):
    print("hello 大家好")
    print("我叫{0},我今年{1}大了".format(name,age))
    if hobby=="没有":
        print("我没有爱好")
    else:
        print("我的爱好是{0}".format(hobby))

    print("*"*20)
    for i in args:
        print(i)
    for k,v in kwargs.items(): #遍历字典需要items()方法
        print(k,'----',v)

fun(name="zhangsan",age=19)

fun("张三",19,"有","游戏","画画",sd="阅读",sw="写作")

#收集参数的解包问题
#把参数放入list或字典中，直接把list/dist中的值放入参数中
def fun(*args):
    print("hahah")
    for i in args:
        print(i)
fun("zhagnsan","李四",19,20)

l=list()
l.append("张三")
l.append("李四")
l.append(19)
l.append(20)
fun(l) #此时args的表示形式是字典内的一个list的元素，即args=({})
#此时调用需要用一个星号进行解包
fun(*l)

#函数文档
def fun(name,age,*args):
   '''
   :param name: 
   :param age: 
   :param args: 
   :return: 
   ''''''
    print('这是一个函数文档')
help(fun)
fun.__doc__