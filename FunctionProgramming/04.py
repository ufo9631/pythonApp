#高级函数补充 zip:合并两个可迭代的内容生成一个可迭代的tuple元素类型组成的内容
l1=[1,2,3,4,5]
l2=[11,22,33,44,55]
z=zip(l1,l2)
print(type(z))
print(z)

for i in z:
    print(i)

l1=['wangwang','mingyue','yyt']
l2=[89,23,78]
z=zip(l1,l2)
for i in z:
    print(i)
l3=[i for i in z]
print(l3) #思考为什么会有空

#enumerate 案例1
#跟zip功能相似
#对可迭代对象里的每一个元素，配上一个索引，然后索引和内容构成tuple类型
l1=[11,22,33,44,55]
em=enumerate(l1)
l2=[i for i in em]
print(l2)

#案例2
em=enumerate(l1,start=100) #指定索引从100开始
print([i for i in em])

#collections模块
#namedtuple
#deque
#tuple类型
#是一个可命名的tuple
import collections
#help(collections.namedtuple)
Point=collections.namedtuple("Point",['x','y'])
p=Point(11,22)
print(p.x)
print(p[0])

Circle=collections.namedtuple("Circle",['x','y','r'])
c=Circle(100,150,50)
print(c)
print(isinstance(c,tuple))

#deque
#比较方便的解决频繁删除插入带来的效率问题
from collections import deque
q=deque(['a','b','c'])
print(q)
q.append("d")
print(q)
q.appendleft("x")
print(q)

#defaultdict
#当直接读取dict不存在的属性时，直接返回默认值
from collections import defaultdict
func=lambda :"liudana" #lambda表达式，直接返回字符串
d1=defaultdict(func)#{"one":1,"two":2,"three":3}
d1["one"]=1
d1["two"]=2
print(d1['one'])
print(d1["four"])

#counter
#统计字符串个数
from collections import Counter
c=Counter("abcdefgefabcdefgefabcdefgef")
print(c)

s=["liudana",'zhangsan','loev','vic']
c=Counter(s)
print(c)