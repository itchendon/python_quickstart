import socket
# 创建socket对象
sk = socket.socket();
# 绑定ip和端口号码
sk.bind(("0.0.0.0",8999))
# 设置监听
sk.listen(5)
# 等待客户端连接
conn,addr = sk.accept();
print(conn)
print(addr)
while True:
    acceptData = conn.recv(1024);
    print("收到客户端发送的内容:",acceptData.decode("utf-8"))
    sendData = "收到你的内容了！！！";
    conn.send(sendData.encode("utf-8"))