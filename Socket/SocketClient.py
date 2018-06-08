import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 999

s.connect((host, port))
# 接收小于1024字节的数据
msg = s.recv(1024)

s.close()

print(msg.decode('utf-8'))
