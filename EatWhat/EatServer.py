import socket
import threading
import time
import random

# 创建socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口
s.bind(('127.0.0.1', 9999))
s.listen(4)
print("Waiting for connection...")
foods = ['南云上品', '鸭血粉丝汤', '浏阳小碗菜', '嗨大米', '驴肉火烧']
choose_foods = []

def tcplink(sock, addr):
    print('欢迎来自毅弘的铂金大神 %s:%s' % addr)
    sock.send(('欢迎来自毅弘的铂金大神 %s%s,'
               '今天您中午想去哪里觅食？' % addr).encode('utf-8'))
    now = time.time()
    while ((time.time() - now) < 120 ):
        sock.send(('你还有%s秒的考虑时间' %
                   int(120 - (time.time() - now))).encode('utf-8'))
        food = sock.recv(1024).decode('utf-8')
        time.sleep(1)
        if food is not None:
            choose_foods.append(food)
            sock.send('你已经投票，请等待他人选择'.encode('utf-8'))
            break
        if len(choose_foods) == 4:
            break
    if len(choose_foods) > 0:
        index = random.randint(len(choose_foods))
        sock.send(('今天的食物是%s' % foods[index]).encode('utf-8'))
        sock.send(('想吃什么只有明天再选择了88').encode('utf-8'))
    else:
        index = random.randint(4)
        sock.send(('今天的食物是%s' % foods[index]).encode('utf-8'))
        sock.send(('想吃什么只有明天再选择了88').encode('utf-8'))
    sock.close()


while True:
    sock, addr = s.accept()
    # 创建线程来接收消息
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()


