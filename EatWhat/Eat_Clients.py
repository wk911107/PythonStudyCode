import socket
import threading
import time


# 创建socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print(s.recv(1024).decode('utf-8'))
now = time.time()
s.send(input().encode('utf-8'))
while True:
    t = threading.Thread(print(s.recv(1024).decode('utf-8')))
    t.start()
