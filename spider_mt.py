#!/usr/bin/python
# -*- coding:utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from mt.items import MtItem
import os
import sys
import pymysql
reload(sys)
sys.setdefaultencoding('utf-8')
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

class spider_mt(scrapy.Spider):
    name = 'mt'
    start_urls = ['http://hf.meituan.com/jiankangliren/']
    allowd_domain = 'hf.meituan.com'
    conn = pymysql.connect(host='192.168.3.232', user='zwj', passwd='123456', db='caiji', charset='utf8')
    cursor = conn.cursor()

    def parse(self, response):
        for i in range(0,29):
            url = 'http://hf.meituan.com/jiankangliren/pn'+str(i+1)
            yield Request(url, callback=self.getUrl)

    def getUrl(self,response):
        xp = Selector(response)
        div = xp.xpath('//div[@class="list-item-desc-top"]/a/@href')
        for i in range(0, len(div)):
            href = 'http:' + ''.join(
                xp.xpath('//div[@class="list-item-desc-top"]/a/@href')[i].extract())
            sql = 'select href from TOP_MEITUANLR where href="%s"'%href
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            if len(rs)==0:
                id = href.split('/')[-2]
                pcomnu = xp.xpath('//span[@class="highlight"]/text()')[i].extract()
                comnu = ''.join(pcomnu).strip('人评论')
                yield Request(href, meta={'id':id, 'comnu':comnu, 'href':href}, callback=self.detailPage)
            else:
                continue

    def detailPage(self,response):
        item = MtItem()
        hx = Selector(response)
        name = ''.join(hx.xpath('//h1[@class="seller-name"]/text()').extract())
        addr = ''.join(hx.xpath('//div[@class="item"][1]/a/span/text()').extract())
        phone = ''.join(hx.xpath('//div[@class="item"][2]/span[2]/text()').extract())
        on_time = ''.join(hx.xpath('//div[@class="item"][3]/span[2]/text()').extract())
        comnu = response.meta['comnu']
        shopid = response.meta['id']
        href = response.meta['href']
        score = ''.join(hx.xpath('//span[@class="score"]/text()').extract())
        item['href'] = href
        item['name'] = name
        item['addr'] = addr
        item['phone'] = phone
        item['on_time'] = on_time
        item['score'] = score
        item['comnu'] = comnu
        item['shopid'] = shopid
        item['cjmc'] = '丽人'
        if len(name)==0:
            pass
        else:
            yield item


