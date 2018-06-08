from bs4 import BeautifulSoup
from urllib import request


if __name__ == '__main__':
    download_url = 'http://www.biqukan.com/1_1094/5403177.html'
    head = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/'
                          'MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/66.0.3359.181 Mobile Safari/537.36'}
    # 创建request对象，并模拟用户代理
    download_req = request.Request(url=download_url, headers=head)
    # 获得回应
    download_response = request.urlopen(download_req)
    download_html = download_response.read().decode('gbk', 'ignore')
    # print(download_html)
    soup_texts = BeautifulSoup(download_html, 'lxml')
    texts = soup_texts.find_all(id='content', class_='showtxt')
    # print(type(texts))
    soup_text = BeautifulSoup(str(texts), 'lxml')
    # 打印在控制台上内容不全，但是输出到文件中能完全显示
    print("*********************")
    print(soup_text.div.text)

    with open(r'C:\Users\u\Desktop\book.txt', 'wb') as f:
        f.write(soup_text.div.text.replace('\xa0', '').encode('utf-8'))
    print('下载完成')
