from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import requests
import os
import time

if __name__ == '__main__':
    list_url = []
    head = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build'
                          '/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/66.0.3359.181 Mobile Safari/537.36'}
    for num in range(1, 20):
        if num == 1:
            url = 'http://www.shuaia.net/index.html'
        else:
            url = 'http://www.shuaia.net/index_%d.html' % num
        req = requests.get(url, headers=head)
        req.encoding = 'utf-8'
        html = req.text
        bf = BeautifulSoup(html, 'lxml')
        target_url = bf.find_all(class_='item-img')

        for each in target_url:
            url = each.img.get('alt') + '=' + each.get('href')
            list_url.append(url)
            # print(url)
    print('连接采集完成！')

    for each_img in list_url:
        img_info = each_img.split('=')
        target_url = img_info[1]
        filename = img_info[0] + '.jpg'
        img_req = requests.get(target_url, head)
        # print(img_req)
        img_req.encoding = 'utf-8'
        img_html = img_req.text
        img_bf_1 = BeautifulSoup(img_html, 'lxml')
        img_url = img_bf_1.find_all('div', class_='wr-single-content-list')
        img_bf_2 = BeautifulSoup(str(img_url), 'lxml')
        img_url = 'http://www.shuaia.net' + img_bf_2.div.img.get('src')
        if 'images' not in os.listdir():
            os.makedirs('images')
        urlretrieve(img_url, filename='images/' + filename)
        time.sleep(1)
    print('下载完成！')