
import time
import threading
def loop1():
    print("start loop 1 at:",time.ctime())
    time.sleep(3)
    print("end loop 1 at:",time.ctime())
def loop2():
    print("start loop 2 at:",time.ctime())
    time.sleep(4)
    print("end loop 2 at:",time.ctime())
def loop3():
    print("start loop 3 at:",time.ctime())
    time.sleep(5)
    print("end loop 3 at:",time.ctime())
def main():
    print("Start at:",time.ctime())
    t1=threading.Thread(target=loop1,args=())
    t1.setName("THR_1")
    t1.start()

    t2=threading.Thread(target=loop2,args=())
    t2.setName("THR_2")
    t2.start()

    t3=threading.Thread(target=loop3,args=())
    t3.setName("THR_3")
    t3.start()

    time.sleep(3)
    for thr in threading.enumerate():
        print("正在运行的线程名字是:{0}".format(thr.getName))

    print("正在运行的子线程数量为：{0}".format(threading.activeCount()))
    print("All done at:",time.ctime())

if __name__=='__main__':
    main()
    #一定要有while语句
    #因为启动多线程后本程序就作为主线程存在
    #如果主线程执行完毕，则子线程可能也需要终止
    while True:
        time.sleep(10)