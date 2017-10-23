# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

class MtPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host='192.168.3.232',user='zwj',passwd='123456',db='caiji',charset='utf8')
        cursor = conn.cursor()
        sql_insert = 'insert into TOP_MEITUANLR(NAME,HREF,SCORE,ADDR,PHONE,ON_TIME,CJMC,SHOPID,COMNU) VALUES("%s","%s","%s","%s","%s","%s","%s","%s","%s")'%\
                     (item['name'],item['href'],item['score'],item['addr'],item['phone'],item['on_time'],item['cjmc'],item['shopid'],item['comnu'])
        print(sql_insert)
        cursor.execute(sql_insert)
        conn.commit()

        cursor.close()
        conn.close()
        return item
