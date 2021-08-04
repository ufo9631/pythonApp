#coding=utf-8
import pygame
import os
import time
from pygame.locals import *

current_path=os.getcwd()
imagePath=current_path+"/App1/pythonApp/test/飞机大战/images/"

#飞机类
class HeroPlane(object):
    def __init__(self,screen_temp):
        #super().__init__()
        self.x=210
        self.y=600
        self.screen=screen_temp
        self.image=pygame.image.load(imagePath+"life.png")
        self.bullet_list=[] #存储发射出去的对象引用

    #飞机显示
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

    #飞机向左移动
    def move_left(self):
        self.x-=5
    #飞机向右移动
    def move_right(self):
        self.x+=5

    #飞机开火
    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))


#定义子弹类

class Bullet(object):
    def __init__(self,screen_temp,x,y):
        #super().__init__()
        self.x=x+20
        self.y=y-20
        self.screen=screen_temp
        self.image=pygame.image.load(imagePath+"bullet2.png")

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

    def move(self):
        self.y-=1




def key_control(hero):
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type==KEYDOWN:#判断是否按下了键
            #检测按键是否是a或者left
            if event.key==K_a or event.key==K_LEFT:
                print('left')
                #x-=5
                hero.move_left()
            elif event.key==K_d or event.key==K_RIGHT:#检测是否是按了d或者right
                print("right")
                #x+=5
                hero.move_right()
            elif event.key==K_SPACE:#检测是否按了空格键
                hero.fire()



def main():
    
   
    

    #1创建窗口
    screen=pygame.display.set_mode((480,650),0,32)

    #2 创建一个和窗口大小一样的图片，用来填充背景
    backgroud=pygame.image.load(imagePath+"background.png")

    #3创建玩家英雄
    #hero=pygame.image.load(imagePath+"life.png")

    #x=210
    #y=600
    hero=HeroPlane(screen)
    while True:

        #设定需要显示的背景图
        screen.blit(backgroud,(0,0))

        hero.display()
        #screen.blit(hero,(x,y))

        #更新需要显示的内容
        pygame.display.update()
        
        key_control(hero)


        time.sleep(0.01)


            

        

if __name__ == '__main__':
    main()
    