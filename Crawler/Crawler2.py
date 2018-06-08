from urllib import request


if __name__ == '__main__':
    req = request.Request('http://fanyi.baidu.com')
    response = request.urlopen(req)
    print('geturl打印信息：%s' % (response.geturl()))
    print('******************************************')
    print('info打印信息：%s' % (response.info()))
