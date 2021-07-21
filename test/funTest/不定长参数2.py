def test(a,b,c=33,*args,**kwargs):
    print("-"*30)
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
    result=a+b
    for num in args:
        result+=num
    print("result=%d"%result)


test(1,22,33,44,55)  #不定参数不带变量名会全部扔到*args


test(1,22,33,66,77,88,task=99,done=89) # 不定参数带变量名会全部扔到**kwargs 里