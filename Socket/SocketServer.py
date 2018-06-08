import socket

# 创建socket对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取本地主机名
host = socket.gethostname()
port = 999
# 绑定端口号
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

while True:
    clientsocket, addr = serversocket.accept()

print('连接地址：%s' % str(addr))

msg = '你好啊！客户端！'
clientsocket.send(msg.encode('utf-8'))
clientsocket.close()
