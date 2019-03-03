
# 多线程的包 threading ，thread有问题，不好用，python3改成了_thread
'''
利用time生成两个函数
顺序调用
计算总的运行时间
'''
import time
import _thread as thread
def loop1():
    print('Start loop 1 at:',time.ctime())
    time.sleep(4)
    print('End loop 1 at:',time.ctime())

def loop2():
    print('Start loop 2 at:',time.ctime())
    time.sleep(4)
    print('End loop 2 at:',time.ctime())

def main():
    print("Starting at:",time.ctime())
    loop1()
    loop2()
    print("All done at:",time.ctime())
if __name__=='__main__':
    main()