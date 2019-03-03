import socket
def main():
    #1.创建套接字
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #2.绑定一个本地信息
    localaddr=("",7788) #第一个参数为空字符串表示本机任意一个ip
    udp_socket.bind(localaddr)
    while True:
        #03.接收数据
        recv_data=udp_socket.recvfrom(1024)
        recv_msg=recv_data[0]  #存储发送的信息
        send_addr=recv_data[1] #发送方的地址信息
        #04.打印接收到的数据
        print('%s:%s'%(str(send_addr),recv_msg.decode('utf-8')))
    #05.关闭套接字
    udp_socket.close()
if __name__=='__main__':
    main()