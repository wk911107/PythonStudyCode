from urllib import request
from urllib import parse
import time
import hashlib
import random
import json


print('*****************************')
while(True):
    print('请输入需要翻译的单词：')
    word = input()
    if word == 'quit':
        print('程序退出！')
        print('*******************************')
        break

    s = 'fanyideskweb'
    d = 'ebSeFb%=XZ%T[KZ)c(sy!'
    url = 'http://fanyi.youdao.com/translate?smartresult=dictsmartresult=rule'

    salt = str(int(time.time() * 1000)) + str(random.randint(1, 10))
    sign = hashlib.md5((s + word + salt + d).encode('utf-8')).hexdigest()
    Form_Data = {
        'i': word,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskword',
        'salt': salt,
        'sign': sign,
        'doctype': 'json',
        'version': 2.1,
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': False
    }
    Form_Data = parse.urlencode(Form_Data).encode('utf-8')
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit\
            /537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'
    }
    req = request.Request(url, headers=head)
    response = request.urlopen(req, Form_Data)
    html = response.read().decode('utf-8')
    translate_result = json.loads(html)
    translate_result = translate_result['translateResult'][0][0]['tgt']
    print('翻译的结果是<<%s>>' % (translate_result))
