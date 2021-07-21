# lambda 参数:式子
# func= lambda x,y:x+y
def test(a,b):
    a+b
result1=test(11,22)
print("result1=%s"%result1)
#定义一个匿名函数,默认带有return,匿名函数相当于在return后面写表达式
func=lambda a,b:a+b
result2=func(11,22)
print("result2=%d"%result2)

stus=[
    {"name":"王五","age":20},
    {"name":"张三","age":18},
    {"name":"李四","age":19},
    
]
stus.sort(key=lambda x:x["name"])
print(stus)