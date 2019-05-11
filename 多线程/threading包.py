'''
threading的使用
 -直接利用threading.Thread生成Thread实例
 1.t=threading.Thread(target=xxx,args=(xxx,))
 2.t.start():启动线程
 3.t.join():等待多线程执行完成
 4. 守护线程-daemon  
    - 如果在程序中将子线程设置成守护线程，则子线程会在主线程结束的时候自动退出
    - 一般认为，守护线程不重要或者不允许离开主线程独立存在
    - 守护线程跟环境有关
     案例：03.py  04.py
 5.线程常用属性 05.py
 threading.currentThread:返回当前线程变量
 threading.enumerate:返回一个包含正在运行的线程的list,正在运行的线程只的是线程启动后，结束前
 threading.activeCount:返回正在运行的线程数量，效果跟len(threading.enumerate)相同
 threading.setName:给线程设置名字
 threading.getName:得到线程名字 


 直接继承自threading.Thread
  - 直接继承Thread
  - 重写run函数
  - 累实力可以直接运行 案例06.py      
'''

import time
import threading
def loop1(in1):
    print('Start loop 2 at:',time.ctime())
    print("我是参数",in1)
    time.sleep(4)
    print('End loop 2 at:',time.ctime())
def loop2(in1,in2):
    print('Start loop 2 at:',time.ctime())
    print("我是参数",in1,"和参数",in2)
    time.sleep(2)
    print('End loop 2 at:',time.ctime())

def main():
    print("Starting at:",time.ctime())
    t1=threading.Thread(target=loop1,args=("王老大",))
    t1.start()
    t2=threading.Thread(target=loop2,args=("王大鹏","王小鹏"))
    t2.start()
    print("All done at:",time.ctime())

def mainJoin():
    print("Starting at:",time.ctime())
    t1=threading.Thread(target=loop1,args=("王老大",))
    t1.start()
    t2=threading.Thread(target=loop2,args=("王大鹏","王小鹏"))
    t2.start()

    t1.join()
    t2.join()

    print("All done at:",time.ctime())

if __name__=='__main__':
    mainJoin()
    #一定要有while语句
    # 因为启动多线程后本程序就作为主线程存在
    #如果主线程执行完毕，则子线程可能也需要终止
    while True:
        time.sleep(10) # 这边不让主线程等待 那么多线程内的函数不会执行完，主线程执行完后会直接退出