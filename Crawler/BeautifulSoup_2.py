from urllib import request
from bs4 import BeautifulSoup

if __name__ == '__main__':
    target_url = 'http://www.biqukan.com/1_1094/'
    head = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus '
                          '5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like '
                          'Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36'}
    target_req = request.Request(target_url, headers=head)
    target_response = request.urlopen(target_req)
    target_html = target_response.read().decode('gbk', 'ignore')
    # 创建BeautifulSoup对象
    listmain_soup = BeautifulSoup(target_html, 'lxml')
    # 搜索文档树找出div标签中class为listmain的所有子内容
    chapters = listmain_soup.find_all('div', class_='listmain')
    # 使用查询结果再创建一个BeautifulSoup对象，对其继续进行解析
    download_soup = BeautifulSoup(str(chapters), 'lxml')
    begin_flag = False
    # 遍历dl标签下所有子节点
    for child in download_soup.dl.children:
        # 去除回车
        if child != '\n':
            # 找到《一念永恒》正文卷,使能标志位
            if child.string == u"《一念永恒》正文卷":
                begin_flag = True
            # 爬取链接
            if begin_flag and child.a is not None:
                download_url = "http://www.biqukan.com" + child.a.get('href')
                download_name = child.string
                print(download_name + " : " + download_url)
