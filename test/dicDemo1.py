info={"name":"laowang","age":18}
print(len(info))  # key的个数
print(info.keys()) #输出所有的key
print(info.values()) #输出所有的value

print(info.items())

a=(11,22,33)
b,c,d=a   #如果用多个变量来进行赋值，那么元组会依次变量的个数把相应的值赋值过去,多个变量的个数必须跟元组的数量相同
print("a=%s,c=%s"%(b,c))