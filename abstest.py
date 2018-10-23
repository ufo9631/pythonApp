def my_abs(x):
    if x>=0:
        return x
    else:
        return -x

def my_a(x):
    print(x)

def nop():
    pass  #空函数可以用pass定义

def my_b(x):
    if not isinstance(x,(int,float)):  #isinstance 检查数据类型 检查参数是否是整数或是浮点数
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x