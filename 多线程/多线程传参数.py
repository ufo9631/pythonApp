import time
import _thread as thread
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
   
    thread.start_new_thread(loop1,("王老大",))
    thread.start_new_thread(loop2,("王大鹏","王小鹏"))
    print("All done at:",time.ctime())
if __name__=='__main__':
    main()
    while True:
        time.sleep(1) # 这边不让主线程等待 那么多线程内的函数不会执行完，主线程执行完后会直接退出