# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.htm
from naruto import settings
import requests
import os


class NarutospiderPipeline(object):
    def process_item(self, item, spider):
        if 'img_url' in item:
            images = []
            dir_path = '%s/%s' % (settings.IMAGES_STORE, item['dir_name'])
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

            for img_url in item['img_url']:
                # 解析链接，根据链接为图片命名

                prefix = item['link_url'].split('/')[-1].split('.')[0]
                suffix = img_url.split('/')[-1].split('.')[-1]
                # 图片名
                img_file_name = '第' + prefix + '页.' + suffix
                # 图片路径
                img_file_path = dir_path + "/" + img_file_name
                images.append(img_file_path)
                if os.path.exists(img_file_path):
                    continue

                with open(img_file_path, 'wb') as f:
                    response = requests.get(url=img_url)
                    for block in response.iter_content(1024):
                        if not block:
                            break
                        f.write(block)
            item['img_paths'] = images
        return item
