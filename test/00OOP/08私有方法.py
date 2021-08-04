class Dog:
    def __init__(self,new_name):
        self.name=new_name
        self.__age=0 #定义一个私有的属性，属性的名字__age  两个下划线开头的叫做私有属性

    def __test1(self): #两个下划线开头的表示私有方法
        print('---------1---------')
        
    
    def test2(self): #没加下划线的表示共有方法
        print('---------2---------')
        self.__test1()

dog =Dog("小白")
#dog.__test1() #无法直接调用私有方法
dog.test2()