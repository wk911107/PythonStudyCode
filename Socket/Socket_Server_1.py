import socket
import threading
import time

#创建socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('Waiting for connect......')

def transfer(sock, addr):
    print('Now connection is %s:%s' % addr)
    sock.send(b'Welcome!!')
    while True:
        data = sock.recv(1024)
        time.sleep(5)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello,%s!' % data.decode('utf-8')).encode('utf-8'))
    print('Connection is finished %s:%s' % addr)

while True:
    sock, addr = s.accept()
    t = threading.Thread(target=transfer, args=(sock, addr))
    t.start()