# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    href = scrapy.Field()
    on_time = scrapy.Field()
    addr = scrapy.Field()
    phone = scrapy.Field()
    score = scrapy.Field()
    comnu = scrapy.Field()
    shopid = scrapy.Field()
    cjmc = scrapy.Field()
    pass

