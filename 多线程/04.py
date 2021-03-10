#守护线程
import time
import threading
def fun():
    print("Start fun")
    time.sleep(2)
    print("end fun")
print("Main thread")
t1=threading.Thread(target=fun,args=())
t1.setDaemon(True) #设置成守护进程,设置成守护进程需要在进程启动前设置
t1.start()

time.sleep(1)
print("Main thread end")