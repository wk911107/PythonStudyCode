#!usr/bin/python3
#-*-coding:utf-8-*-
"""
煎蛋网妹子图片爬取程序
页数过大后，会出现异常还带修改
"""
import os

from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import requests
import hashlib
import base64
import re
import time


def get_url(code):
    return base64_decode(code).decode('utf-8')
"""
def get_url(n, t=''):
   
    获取解密后的url地址,上个版本
    :param n:
    :param t:
    :param e:
    :return:url地址
 
    f = 'DECODE'
    r = 4
    t = _md5(t)
    # d = n
    p = _md5(t[0:16])
    # o = _md5(t[16:16 + 16])
    m = n[0:r]
    c = p + _md5(p + m)
    n = n[r:]
    e = base64_decode(n)
    k = list(range(256))
    b = [ord(c[g % len(c)]) for g in range(256)]

    h = 0
    for g in range(0, 256):
        h = (h + k[g] + b[g]) % 256
        tmp = k[g]
        k[g] = k[h]
        k[h] = tmp

    u = ''
    q, g = 0, 0
    for h in range(len(e)):
        q = (q + 1) % 256
        g = (g + k[q]) % 256
        tmp = k[q]
        k[q] = k[g]
        k[g] = tmp
        u += chr(e[h] ^ (k[(k[q] + k[g]) % 256]))
    u = u[26:]
    return u
    return base64_decode(n).decode('utf-8')
"""

def _md5(value):
    """MD5加密"""
    md = hashlib.md5()
    md.update(value.encode('utf-8'))
    return md.hexdigest()


def base64_decode(value):
    """
    base64解密，补齐=避免Incorrect padding Error
    :param value: 需要解码的数据
    :return: 解码后的数据
    """
    missing_padding = 4 - len(value) % 4
    if missing_padding:
        value += '='*missing_padding
    return base64.b64decode(value)


def get_code(url):
    """
    获取js中的code
    :param url:js的地址
    :return:code
    """
    content = requests.get(url)
    content.encoding = 'utf-8'
    print(content.text)
    code = re.findall('c=[\w\d]+\(e,"(.*?)"\)',content.text)[0]
    return code


def get_html(url):
    """
    获取html
    :param url:
    :return:
    """
    header = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/'
                            'MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/66.0.3359.181 Mobile Safari/537.36'}
    target_req = requests.get(url, headers=header)
    target_req.encoding = 'utf-8'
    return target_req.text


def get_html_collection(count):
    """
    获取下个页面的html的集合
    :param count:
    :return:
    """
    html_collection = [get_html('http://i.jandan.net/ooxx/')]
    for g in range(count):
        html = html_collection[-1]
        soup = BeautifulSoup(html, 'lxml')
        urls = soup.find_all('a', class_='previous-comment-page')
        url = 'http:' + BeautifulSoup(str(urls), 'lxml').a.get('href')
        html_collection.append(get_html(url))
    return html_collection

if __name__ == "__main__":
    count = input('输入你想爬取的页数(不要太贪心)：')
    html_collection = get_html_collection(int(count))
    index = 1
    for g in html_collection:
        target_soup = BeautifulSoup(g, 'lxml')
        n = target_soup.find_all('span', class_='img-hash')
        img_url = []
        for each in n:
            img_url.append('http:' + get_url(each.string))
        if 'image' not in os.listdir():
            os.makedirs('image')

        for url in img_url:
            urlretrieve(url, filename='image/' + str(index) + '.jpg')
            index += 1
            time.sleep(2)
    print('下载完成！')