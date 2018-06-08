
# -*- coding: utf-8 -*-
# @File  : comic_spider.py
# @Author: WangK
# @Date  : 2018/6/6
# @Desc  : 爬取火影忍者漫画的软件
import scrapy
from naruto.items import NarutoSpiderItem
from scrapy import Selector
import re


class ComicSpider(scrapy.Spider):
    name = 'comic'

    def __init__(self):
        # 图片链接的Server域名
        self.img_server = 'http://n5.1whour.com/'
        # 章节链接的Server域名
        self.link_server = 'http://comic.kukudm.com'
        self.allowed_domains = ['comic.kukudm.com']
        # 爬虫开始的地址
        self.start_urls = ['http://comic.kukudm.com/comiclist/3/']
        self.img_pattern = re.compile(r'\+"(.+)\'><span')

    # 发送请求
    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):
        hxs = Selector(response)
        items = []
        # 章节链接地址
        urls = hxs.xpath('//dd/a[1]/@href').extract()
        # 章节名
        dir_names = hxs.xpath('//dd/a[1]/text()').extract()
        for index in range(len(urls)):
            item = NarutoSpiderItem()
            item['link_url'] = self.link_server + urls[index]
            item['dir_name'] = dir_names[index]
            items.append(item)
        for item in items:
            yield scrapy.Request(url=item['link_url'],
                                 meta={'item': item}, callback=self.parse1)

        # 解析获得章节第一页的页码数和图片链接
    def parse1(self, response):
        # 接收传递的item
        item = response.meta['item']
        item['link_url'] = response.url
        hxs = Selector(response)
        # 获取章节的第一页的图片链接
        pre_img_url = hxs.xpath('//script/text()').extract()
        img_url = [self.img_server + re.findall(self.img_pattern,
                                                pre_img_url[0])[0]]
        # 将获取的图片url赋给item
        item['img_url'] = img_url
        # 返回item，交给item pipeline下载图片
        yield item
        # 获取章节的页数
        page_count = hxs.xpath('//td[@valign="top"]/text()').re(u'共(\d+)页')[0]
        # 根据页数，整理出本章节其他页面的链接
        pre_link = item['link_url'][:-5]
        for each in range(2, int(page_count) + 1):
            new_link = pre_link + str(each) + '.htm'
            yield scrapy.Request(url=new_link, meta={'item': item},
                                 callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        item['link_url'] = response.url
        hxs = Selector(response)
        pre_img_url = hxs.xpath('//script/text()').extract()
        img_url = [self.img_server + re.findall(self.img_pattern,
                                                pre_img_url[0])[0]]
        # 将获取的图片url赋给item
        item['img_url'] = img_url
        # 返回item，交给item pipeline下载图片
        yield item
