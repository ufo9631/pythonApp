import socket
def main():
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    dest_ip=input("请输入对方ip:")
    dest_port=int(input("请输入对方的port:"))
    #从键盘获取数据    
    send_data=input("请输入数据:")
    #如果输入的是exit则退出
   
    #udp_socket.sendto(b"hahaha",("127.0.0.1",8080))
    udp_socket.sendto(send_data.encode('utf-8'),(dest_ip,dest_port))
    #关闭套接字
    udp_socket.close()
    print("--run---")
if __name__=='__main__':
    main()