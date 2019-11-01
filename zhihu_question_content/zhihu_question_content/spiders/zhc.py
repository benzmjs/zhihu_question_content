# -*- coding: utf-8 -*-
import scrapy


class ZhcSpider(scrapy.Spider):
    name = 'zhc'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    def parse(self, response):
        pass
