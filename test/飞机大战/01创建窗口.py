import pygame
import os
import time
def main():
    
    current_path=os.getcwd()
    imagePath=current_path+"/App1/pythonApp/test/飞机大战/images/background.png"
    open(imagePath)

    #1创建窗口
    screen=pygame.display.set_mode((480,852),0,32)

    #2 创建一个和窗口大小一样的图片，用来填充背景
    backgroud=pygame.image.load(imagePath)

    #3 把背景图片放到窗口中显示
    while True:

        #设定需要显示的背景图
        screen.blit(backgroud,(0,0))

        #更新需要显示的内容
        pygame.display.update()
        
        time.sleep(0.01)

if __name__ == '__main__':
    main()
    