
class Person(object):
    def __str__(self):
        if self.gun:
            return "%s的血量为%d，他有枪,%s"%(self.name,self.hp,self.gun)
        else:
            if self.hp>0:
                return "%s的血量为%d,他没有枪"%(self.name,self.hp)
            else:
                return "%s 已挂..."
    #人的类 
    def __init__(self,name):
        super().__init__()
        self.name=name
        self.gun=None #定义变量，用来保存枪的引用
        self.hp=100
    def anzhuang_zidan(self,dan_jia_temp,zi_dan_temp):
        #把子弹安装到弹夹中
        dan_jia_temp.baocun_zidan(zi_dan_temp)

    def anzhuang_danjia(self,gun_temp,danjia_temp):
        #把弹夹安装到枪中
        gun_temp.baocun_danjia(danjia_temp)

    def naqiang(self,gun_temp):
        #拿枪
        self.gun=gun_temp

    def kou_ban_ji(self,diren):
        #让枪发射子弹打敌人
        self.gun.fire(diren)

    def diao_xue(self,sha_shang_li):
        #根据相应的杀伤力掉血
        self.hp-=sha_shang_li
        

#枪类
class Gun(object):

    def __str__(self):
        if self.danjia:
            return "枪的信息为:%s,%s"%(self.name,self.danjia)
        else:
            return "枪的信息为:%s,这把枪没有子弹"%self.name
        

    def __init__(self,name):
        super().__init__()
        self.name=name
        self.danjia=None #用来记住弹夹的引用
        
    def baocun_danjia(self,danjia_temp):
        self.danjia=danjia_temp

    def fire(self,diren):
        #发射子弹,从弹夹取一发子弹，然后让子弹去击中敌人
        
        #1从弹夹取子弹
        zidan_temp=self.danjia.tanchu_zidan()
        #2当子弹去伤害敌人
        if zidan_temp:
            zidan_temp.dazhong(diren)
        else:
            print("弹夹中没有子弹了。。。。")

#弹夹类
class Danjia(object):

    def __str__(self):
        return "弹夹的信息为:%d/%d"%(len(self.zidan_list),self.max_num)
        

    def __init__(self,max_num):
        super().__init__()
        self.max_num=max_num
        self.zidan_list=[]# 用来记录子弹的引用

    def baocun_zidan(self,zi_dan_temp):
        #将子弹保存   
        self.zidan_list.append(zi_dan_temp)

    def tanchu_zidan(self):
        #弹出最上面的子弹
        if self.zidan_list:
            return self.zidan_list.pop()
        else:
            return None

class Zidan(object):
    def __init__(self,sha_shang_li):
        super().__init__()
        self.sha_shang_li=sha_shang_li
    
    def dazhong(self,diren):
        #当敌人掉血,掉一个子弹威力的血
        diren.diao_xue(self.sha_shang_li)
        


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
    for i in range(10):
        #4.创建一些子弹
        zi_dan=Zidan(10)
        #5.老王把子弹安装到弹夹中
        laowang.anzhuang_zidan(dan_jia,zi_dan)

    #6.老王把弹夹安装到枪中
    laowang.anzhuang_danjia(ak47,dan_jia)
    
    #测试弹夹信息
   # print(dan_jia)
    #测试枪信息
   # print(ak47)
    #7.老王拿枪
    laowang.naqiang(ak47)

    print(laowang)
    #8. 创建一个敌人
    gebi_laosong=Person("隔壁老宋")
    print(gebi_laosong)
    #9.老王开枪打敌人
    laowang.kou_ban_ji(gebi_laosong)
    print(gebi_laosong)
    print(laowang)


if __name__ == '__main__':
    main()
    