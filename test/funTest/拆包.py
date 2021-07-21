def test(a,b,c=33,*args,**kwargs):
    print("-"*30)
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
    

A=(4,5,6)
B={"name":"zhangsan","age":18}
test(1,22,33,44,55)  #不定参数不带变量名会全部扔到*args



# 如果参数传的是元组或是字典，那么就需要在元组前面加一个*号，在字典前面加两个*号 ，加*号就是拆包 ，
#如果没有写*号，那么参数会通通放到args里
test(1,22,33,*A,**B)
