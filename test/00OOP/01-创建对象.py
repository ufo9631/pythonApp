class Cat:
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
tom=Cat()
tom.eat()
tom.drink()
#给tome指向的对象添加2个属性
tom.name="汤姆"
tom.age=40
# print("%s的年龄是%d"%(tom.name,tom.age))
tom.introduce()

lanmao=Cat()  
lanmao.name="蓝猫"
lanmao.age=41

lanmao.introduce()