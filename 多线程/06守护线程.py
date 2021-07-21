'''
threading的使用
 -直接利用threading.Thread生成Thread实例
 1.t=threading.Thread(target=xxx,args=(xxx,))
 2.t.start():启动线程
 3.t.join():等待多线程执行完成
 4.守护线程-daemon
  -如果在程序中将子线程设置成守护线程，则子线程会在主线程结束的时候自动退出
  - 一般认为，守护线程不重要，或者不允许离开主线程独立运行
  - 守护线程能否有效跟环境有关
'''

import time
import threading
def fun():
    print("start fun")
    time.sleep(2)
    print("end fun")
t1=threading.Thread(target=fun,args=())
t1.setDaemon(True)
#t1.daemon=True #设置守护线程的另外一种方式
t1.start()

time.sleep(1)
print("Main thread end")
