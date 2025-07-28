import socket
# 创建soket对象
sk = socket.socket()
# 连接服务器
sk.connect(("127.0.0.1",8999))
'''
<socket.socket fd=380, family=2, type=1, proto=0, laddr=('127.0.0.1', 8999), raddr=('127.0.0.1', 52065)>
('127.0.0.1', 52065)
'''
while True:
    sendData = input("请输入你要发送的数据:")
    # 发送数据到服务器
    sk.send(sendData.encode("utf-8"))
    # 等待服务器的响应
    acceptData = sk.recv(1024)
    # 打印服务器的响应
    print("接受到的服务器响应：",acceptData.decode('utf-8'))