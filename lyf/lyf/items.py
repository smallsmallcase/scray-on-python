# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LyfItem(scrapy.Item):
    link_url = scrapy.Field()
    img_url = scrapy.Field()  # 图片链接
    image_paths = scrapy.Field()  # 图片保存地址
