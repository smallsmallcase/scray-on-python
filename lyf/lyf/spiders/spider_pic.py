# @Time    : 2017/8/19 8:57
# @Author  : Jalin Hu
# @File    : spider_pic.py
# @Software: PyCharm

import scrapy
from scrapy import Selector
from lyf.items import LyfItem


class Spider_Pic(scrapy.Spider):
    name = 'lyf'

    def __init__(self):
        self.start_urls = ['http://soso.nipic.com/?q=刘亦菲&f=JPG&g=0&w=0&h=0&p=0&or=0&sort=5&k=0&page=1']

    def start_requests(self):
        for page in range(42):
            page += 1
            url = 'http://soso.nipic.com/?q=刘亦菲&f=JPG&g=0&w=0&h=0&p=0&or=0&sort=5&k=0&page=%s' % page
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        hxs = Selector(response)
        items = []
        urls = hxs.xpath('//li[@class="search-works-item"]/a[contains(@title, "刘亦菲")]/@href').extract()
        for index in range(len(urls)):
            item = LyfItem()
            item['link_url'] = urls[index]
            items.append(item)
        for item in items:
            yield scrapy.Request(url=item['link_url'], meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        item['link_url'] = response.url
        hxs = Selector(response)
        image_url = hxs.xpath('//div[@id="static"] [@class="show-img-section overflow-hidden align-center"]/img/@src').extract()
        item['img_url'] = image_url
        yield item
