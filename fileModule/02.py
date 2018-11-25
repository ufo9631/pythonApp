#pickle
#持久化（序列化，持久化）
#把程序运行中的信息保存在磁盘上
#反序列化：序列化的逆过程
#pickle：python提供的序列化模块
#pickle.dump:序列化
#pickle.load：反序列化


#序列化案例

import  pickle
age=19
with open(r"test02.txt",'wb') as f:
    pickle.dump(age,f)
with open(r"test02.txt",'rb') as f:
    age=pickle.load(f)
    print(age)

a=[19,'vic','xia men si ming guan yin shan']
with open(r"test03.txt",'wb') as f:
    pickle.dump(a, f)
with open(r"test03.txt",'rb') as f:
    a=pickle.load(f)
    print(a)

#持久化-shelve
#持久化工具
#类似字典，用kv对数据保存，存取方式跟字典类似
#open,close

#使用shelve创建文件并使用
import shelve
#打开文件，shv相当于一个字典
shv=shelve.open(r"shv.db")
shv["one"]=1
shv["two"]=2
shv["three"]=3
shv.close()
#通过以上案例发现，shelve自动创建的不仅仅是一个shv.db文件还包括其他文件

#shelve读取案例
shv=shelve.open(r"shv.db")
try:
    print(shv["one"])
    print(shv["three"])
finally:
    shv.close()

#shelve特性
#不支持多个应用并行写入
    #为解决这个问题，open的时候可以使用flag=r
#写回问题
    #shelve 恶劣情况下不会等待持久化对象进行任何修改
    #解决方法：强制写回：writeback=True
#shelve：只读方式打开
shv=shelve.open(r"shv.db",flag='r')
try:
    k1=shv["one"]
    print(k1)
finally:
    shv.close()


shv=shelve.open(r"shv.db")
try:
    shv["one"]={"eins":1,"zwei":2,"drei":3}
finally:
    shv.close()

shv=shelve.open(r"shv.db")
try:
    one=shv["one"]
    print(one)
finally:
    shv.close()


#shelve忘记写回，需要使用强制写回
shv=shelve.open(r'shv.db',writeback=True) #writeback一旦有更改会强制写回
try:
    k1=shv["one"]
    print(k1)
    k1['eins']=100 #一旦shelve关闭，则内容还是存在与内存中，没有写回数据库
finally:
    shv.close()


shv=shelve.open(r'shv.db')
try:
    k1=shv["one"]
    print(k1)
finally:
    shv.close()


#shelve 使用with管理上下文环境
with shelve.open(r"shv.db",writeback=True) as shv:
    k1=shv["one"]
    print(k1)
    k1["eins"]=200


with shelve.open(r"shv.db") as shv:
    print(shv["one"])