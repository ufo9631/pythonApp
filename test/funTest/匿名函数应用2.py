def test(a,b,func):
    result=func(a,b)
    print(result)

test(11,22,lambda x,y:x+y)

func_new=input("请输入一个匿名函数:")
func_new=eval(func_new)  #将字符串转为表达式
test(1,2,func_new) #可以直接从外界输入一个匿名函数  