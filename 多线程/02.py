
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
    '''
    启动多线程的意思是用多线程去执行某个函数
    启动多线程的函数为start_new_thread
    两个参数，一个是需要运行的函数名，第二个是函数的参数作为元组使用，为空则使用空元组
    注意：如果函数只有一个参数，需要参数后有一个逗号
    '''
    thread.start_new_thread(loop1,())
    thread.start_new_thread(loop2,())
    print("All done at:",time.ctime())
if __name__=='__main__':
    main()
    while True:
        time.sleep(1) # 这边不让主线程等待 那么多线程内的函数不会执行完，主线程执行完后会直接退出