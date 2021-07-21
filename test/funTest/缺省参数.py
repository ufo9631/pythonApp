def test(a,b=22,c=33):  #  设置默认值的叫做缺省参数
    result=a+b
    print("result=%d"%result)

test(11)
test(11,c=55)  #缺省参数名称要跟定义的名称一样
test(a=10,c=2)