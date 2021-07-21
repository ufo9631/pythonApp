def sum_2_nums(a,b,*args):  #不定长参数一定要放在最后的位置
    print(a)
    print(b)
    print(args)
    result=a+b
    print("result=%d"%result)

sum_2_nums(11,22,1,2,3,4)

# 元组只有一个元素，那么元素后面一定要多加一个逗号这样才能称之为元组，否则不是元组
