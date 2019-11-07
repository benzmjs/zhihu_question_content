# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuQuestionContentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    unlabeled_content = scrapy.Field()
    tagged_content = scrapy.Field()
    title = scrapy.Field()
    marked = scrapy.Field()
    content_image_url = scrapy.Field()
    final_content = scrapy.Field()
