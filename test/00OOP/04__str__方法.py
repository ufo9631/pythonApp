class Cat:
    #初始化对象
    def __init__(self,new_name,new_age): #对象以创建 这个方法就会被自动执行，（构造函数）
        self.name=new_name
        self.age=new_age
        #print("hahahha") 

    def __str__(self): #魔法方法 ,当前对象的描述，必须要用return  ,调用对象时会自动调用此方法 print(tom)
        return "%s的年龄是%d"%(self.name,self.age) 
    #属性

    #方法
    def eat(self):  #self 是当前对象的引用，定义方法必填  self相当于this   名称不一定要叫self 可以是任意变量名，方法至少要有一个参数
        print("猫在吃鱼")
            
    def drink(self):
        print("猫在喝水")

    def introduce(self):
        #print("%s的年龄是%d"%(tom.name,tom.age))
        print("%s的年龄是%d"%(self.name,self.age))

#创建对象
tom=Cat("汤姆",40)

lanmao=Cat("蓝猫",10)  

print(tom)
print(lanmao)