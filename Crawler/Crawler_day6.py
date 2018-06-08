from urllib import request
from http import cookiejar

if __name__ == '__main__':
    # 声明一个CookieJar对象实例来保存cookie
    cookie = cookiejar.CookieJar()
    # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器
    cookie_handler = request.HTTPCookieProcessor(cookie)
    # 通过CookieHandler创建opener
    opener = request.build_opener(cookie_handler)
    response = opener.open('http://www.baidu.com')
    for item in cookie:
        print('Name = %s' % item.name)
        print('Value = %s' % item.value)
