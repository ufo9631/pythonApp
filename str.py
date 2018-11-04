#s=""
#字符串格式化  1.利用百分号(%) 2.利用format函数
s='I love %s'
print(s%'xiaoming')
print('I am %s years old %d'%('xiaoming',10))  #占位符和参数个数必须一样，如果出现多个占位符，对应的参数需要用括号括起来

#使用format推荐使用的方法，使用{}和：代替%号
s='I love {}'.format("chenweichao")
print(s)
s='yes,i am{1} years old,I love {0} and i am {1} years old'.format('vic',28)
print(s)
#None 表示什么都没有，如果函数没有返回值，可以返回None,用来占位置，用来接触变量绑定

#运算符
#1.python没有自增和自减的运算符 ++，--
#2.逻辑运算符 and,or, not
#成员运算符 in ,not in
l=[1,2,3,4]
a=7
b=a in l
print(b)
print(a not in l)
#身份运算符
#1.is 用来检测两个变量是否同一个变量
#2. is not ：两个变量不是同一个变量
a=9
b=9
print(a is b)
a="I loeve chenweichao"
c="I loeve Chenweichao"
print(a is c)