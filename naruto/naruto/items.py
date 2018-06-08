# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy.item import Item,Field


class NarutoSpiderItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 漫画的章节名
    dir_name = Field()
    # 漫画的每页的链接
    link_url = Field()
    # 漫画的图片链接
    img_url = Field()
    # 漫画的保存地址
    img_paths = Field()
