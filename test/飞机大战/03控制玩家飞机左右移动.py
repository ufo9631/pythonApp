#coding=utf-8
import pygame
import os
import time
from pygame.locals import *
def main():
    
    current_path=os.getcwd()
    imagePath=current_path+"/App1/pythonApp/test/飞机大战/images/"
    

    #1创建窗口
    screen=pygame.display.set_mode((480,852),0,32)

    #2 创建一个和窗口大小一样的图片，用来填充背景
    backgroud=pygame.image.load(imagePath+"background.png")

    #3创建玩家英雄
    hero=pygame.image.load(imagePath+"life.png")

    x=210
    y=600
    while True:

        #设定需要显示的背景图
        screen.blit(backgroud,(0,0))

        screen.blit(hero,(x,y))

        #更新需要显示的内容
        pygame.display.update()
        
        for event in pygame.event.get():
    
            if event.type == pygame.QUIT:
                 pygame.quit()
            elif event.type==KEYDOWN:#判断是否按下了键
                #检测按键是否是a或者left
                if event.key==K_a or event.key==K_LEFT:
                    print('left')
                    x-=5
                elif event.key==K_d or event.key==K_RIGHT:#检测是否是按了d或者right
                    print("right")
                    x+=5
                elif event.key==K_SPACE:#检测是否按了空格键
                    print("space")

            

        

if __name__ == '__main__':
    main()
    