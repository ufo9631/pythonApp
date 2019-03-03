import socket
def main():
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #从键盘获取数据
    while True:
        send_data=input("请输入数据:")
        #如果输入的是exit则退出
        if send_data=='exit':
            break
        #udp_socket.sendto(b"hahaha",("127.0.0.1",8080))
        udp_socket.sendto(send_data.encode('utf-8'),("127.0.0.1",8080))
    #关闭套接字
    udp_socket.close()
    print("--run---")
if __name__=='__main__':
    main()