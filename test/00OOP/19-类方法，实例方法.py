class Game(object):
    num=0 #类属性 ，静态变量
    def __init__(self):
        self.name="老王" #实例属性
    @classmethod  #@classmethod 表示它是一个类方法（C#静态方法）
    def add_num(cls):  #类方法必须要有参数，跟实例方法一样必须要有参数 
        cls.num=100
        
    #静态方法,静态方法可以不传参数
    @staticmethod
    def print_menu():
        print("----------------------")
        print("1.穿越火线")
        print("2.开始游戏")
        print("3.结束游戏")
        print("----------------------")


game=Game()
#Game.add_num() #类方法可以通过类的名字调用
game.add_num() #类方法也可以通过这个类创建出来的对象去调用类方法
print(Game.num)  
Game.print_menu() #通过类调用静态方法
game.print_menu() #通过实例调用静态方法