"""
利用BeautifulSoup下载小说
"""
from urllib import request
from bs4 import BeautifulSoup
import sys

if __name__ == "__main__":
    file = open("一念永恒.txt", 'w', encoding='utf-8')
    target_url = 'http://www.biqukan.com/1_1094/'
    head = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus '
                          '5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like '
                          'Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36'}
    target_req = request.Request(target_url, headers=head)
    target_response = request.urlopen(target_req)
    target_html = target_response.read().decode('gbk', 'ignore')
    # 创建BeautifulSoup对象
    listmain_soup = BeautifulSoup(target_html, 'lxml')
    # 搜索文档树
    chapters = listmain_soup.find_all('div', class_='listmain')
    # 使用查询结果再创建一个BeautifulSoup对象，对其继续进行解析
    download_soup = BeautifulSoup(str(chapters), 'lxml')
    # 计数章节个数
    numbers = (len(download_soup.dl.contents) - 1) / 2 - 14
    index = 1
    # 记录正文开始的开关,以及章节名称，避免重复的章节读取
    begin_flag = False
    content_name = None
    # 遍历dl标签下所有子节点
    for child in download_soup.dl.children:
        if child != '\n':
            if child.string == u'《一念永恒》正文卷':
                begin_flag = True
            if begin_flag and child.a is not None:
                if child.string == content_name:
                    index += 1
                    continue
                download_url = 'http://www.biqukan.com' + child.a.get('href')
                download_req = request.Request(download_url, headers=head)
                download_response = request.urlopen(download_req)
                download_html = download_response.read().decode('gbk', 'ignore')
                soup_texts = BeautifulSoup(download_html, 'lxml')
                texts = soup_texts.find_all(id='content', class_='showtxt')
                # print(type(texts))
                soup_text = BeautifulSoup(str(texts), 'lxml')
                content_name = child.string
                file.write(content_name + '\n\n')
                for each in soup_text.div.text.replace('\xa0', ''):
                    if each == 'h':
                        break
                    if each != ' ':
                        file.write(each)
                    if each == '\r':
                        file.write('\n')
                file.write('\n\n')
                # 打印爬取进度
                sys.stdout.write('已下载：%.3f%%' % float(index * 100/numbers)  + '\r')
                sys.stdout.flush()
                index += 1
    file.close()
