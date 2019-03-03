'''
threading的使用
 -直接利用threading.Thread生成Thread实例
 1.t=threading.Thread(target=xxx,args=(xxx,))
 2.t.start():启动线程
 3.t.join():等待多线程执行完成
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
if __name__=='__main__':
    main()
    while True:
        time.sleep(1) # 这边不让主线程等待 那么多线程内的函数不会执行完，主线程执行完后会直接退出