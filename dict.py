#dict字典
#字典是一种组合数据，没有顺序的组合数据，数据以键值对形式出现
#字典的创建
d={}
print(d)
d=dict()
d={"one":1,"two":2,"three":3} #创建有值的字典，每一组数据用冒号隔开，每一对键值对用逗号隔开
print(d)
d=dict(one=1,two=2,three=3)
print(d)
d=dict([("one",1),("two",2),("three",3)])
print(d)
#字典的特征
#字典是序列类型，但是是无序序列，所以没有分片和索引
#字典的数据每个都有键值对组成，即kv对
#key必须是可以哈希的值，比如int,string,float,tuple但是list,set,dict不行
#value:任何值

#字典的常见操作
#访问数据
d={"one":1,"two":2,"three":3}
print(d["one"])
d["one"]="eins"
print(d)

#删除某个操作
#使用del操作
del d["one"]
print(d)
#成员检测,成员检测  检测的是key的内容
d={"one":1,"two":2,"three":3}
if 2 in d:
    print("value")
if "two" in d:
    print("key")
if ("two",2) in d:
    print("kv")

#遍历 py3
#按key来使用for循环
for k in d:
    print(k,d[k])
#上面代码改写
for k in d.keys():
    print(k,d[k])

for v in d.values():
    print(v)

'''
for k,v in d: #无法使用这种方式访问需要加items
    print(k,'-----',v)
'''
for k,v in d.items(): #必须加上items
    print(k,'-----',v)

#字典生成
d={"one":1,"two":2,"three":3}
dd={k:v for k,v in d.items()}
print(dd)

#字典相关函数
#通用函数len,max,min,dict
#   str(字典):返回字典字符串格式
print(str(d))

#clear 字典清空
#items:返回字典的键值对组成的元组格式

i=d.items()
print(type(i))
print(i)
#keys:返回字典的键组成的一个结构
k=d.keys()
print(k)
v=d.values()
print(v)

#get：根据指定键返回相应的值，好处是，可以这是默认值,默认值是None
d={"one":1,"two":2,"three":3}
print(d.get("sdf"))
print(d.get("sdf",100))

#fromkeys:使用指定的序列作为键，使用一个值为字典的所有的键的值
l=["esdf","Vic","dire"]
d=dict.fromkeys(l,"hahaha")
print(d)