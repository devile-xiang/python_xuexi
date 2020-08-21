import socket


if __name__ == '__main__':
    #1.创建tcp客户端套接字
    tcp_client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #2.和服务端套接字建立连接
    tcp_client_socket.connect(("192.168.157.129",8080))
    #3.发送数据到服务器
    send_connect="你好，我是客户端小白！！！"
    #对字符串进行编码，转化成二进制数据
    send_data=send_connect.encode("gbk")
    #windows里面的网络调试助手使用的gbk
    #linux里面的网络调试助手使用的utf-8
    tcp_client_socket.send(send_data)
    #4.接受服务器的数据

    recv_data=tcp_client_socket.recv(1024)
    print(recv_data.decode('gbk'))
    #5.关闭套接字
    tcp_client_socket.close()