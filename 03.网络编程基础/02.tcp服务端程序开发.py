import socket




if __name__ == '__main__':

    #创建tcp服务器套字节
    #socket.AF_INET：ipv4,AF_INET6:ipv6
    tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #绑定端口号
    #第一个参数表示ip地址，一般不懂制定，表示本机任何一个ip即可
    tcp_server_socket.bind(("",8080))
    #设置监听
    #128.表示最大等待建立连接的个数
    tcp_server_socket.listen(128)
    #等待接收客户端的连接请求
    #注意，每次当客户端和服务单建立连接成功回访回一个新的套接字
    #tcp_server_socket 只负责等待接收客户端的连接请求，收发消息不是用该套接字
    new_client,ip_port=tcp_server_socket.accept()
    #接受客户端的数据
    print("客户端的ip和端口号：",ip_port)
    #收发信息都是使用返回的这个新的套接字

    #d对二进制进行接码变成字符串
    recv_data = new_client.recv(1024)
    recv_data=recv_data.decode("gbk")
    print("接收客户端的数据为：", recv_data)
    #发送数据到客户端
    sen_data="你好，问题正在处理中！！！！"
    sen_data=sen_data.encode("gbk")
    new_client.send(sen_data)

    #关闭服务与客户端的套接字，表示和客户端表示终止通信
    new_client.close()
    #关闭套字节
    #关闭服务器套接字，表示服务端以后不再等待接收客户端信息
    tcp_server_socket.close()