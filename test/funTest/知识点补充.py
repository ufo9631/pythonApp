# a=100 值类型参数不会改变
a=[100] #引用类型参数会变
def test(num):
    num+=num
    #num=num+num  跟num+=num 不是一回事，num=num+num 不会改变原始值地址指向，num+=num 会改变参数指针指向
    print("in ----test-----num%d"%num)
test(a)

print(a)