from urllib import request
import chardet

if __name__ == '__main__':
    res = request.Request('http://www.baidu.com')
    req = request.urlopen(res)
    html = req.read()
    # html = html.decode('utf-8')
    chart = chardet.detect(html)
    print(html)
    print(chart)
