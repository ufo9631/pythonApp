
class Person(object):
    #人的类
    def __init__(self,name):
        super().__init__()
        self.name=name
    def anzhuang_zidan(self,dan_jia_temp,zi_dan_temp):
        #把子弹安装到弹夹中
        dan_jia_temp.baocun_zidan(zi_dan_temp)

    def anzhuang_danjia(self,gun_temp,danjia_temp):
        #把弹夹安装到枪中
        gun_temp.baocun_danjia(danjia_temp)

#枪类
class Gun(object):
    def __init__(self,name):
        super().__init__()
        self.name=name
        self.danjia=None #用来记住弹夹的引用
        
    def baocun_danjia(self,danjia_temp):
        self.danjia=danjia_temp
#弹夹类
class Danjia(object):

    def __str__(self,max_num):
        return "弹夹的信息为:%d/%d"%(len(self.zidan_list),self.max_num)
        

    def __init__(self,max_num):
        super().__init__()
        self.max_num=max_num
        self.zidan_list=[]# 用来记录子弹的引用

    def baocun_zidan(self,zi_dan_temp):
        #将子弹保存   
        self.zidan_list.append(zi_dan_temp)

class Zidan(object):
    def __init__(self,sha_shang_li):
        super().__init__()
        self.sha_shang_li=sha_shang_li


def main():
    '''
    用来控制程序流程
    '''
    #1.创建老王对象
    laowang=Person("laowang")
    #2.创建枪对象
    ak47=Gun("AK47")
    #3. 创建一个弹夹对象
    dan_jia=Danjia(20)
    #4.创建一些子弹
    zi_dan=Zidan(10)
    #5.老王把子弹安装到弹夹中
    laowang.anzhuang_zidan(dan_jia,zi_dan)

    #6.老王把弹夹安装到枪中
    laowang.anzhuang_danjia(ak47,dan_jia)

    #测试弹夹信息

    #测试枪信息

    #7.老王拿枪

    #8.老王开枪打敌人

    #9.创建一个敌人
    


if __name__ == '__main__':
    main()
    