class Tool(object):
    #定义属性
    num=0 #类属性，类型与C#的静态变量
    def __init__(self,new_name):
        self.name=new_name
        #对类属性赋值
        Tool.num+=1


tool1=Tool("铁锹")
tool2=Tool("工兵铲")
tool3=Tool("水桶")

print(Tool.num)