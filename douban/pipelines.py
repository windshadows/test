# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import os
from frozen_dir import app_path
class DoubanPipeline(object):
    apppath = app_path() + r'\douban1.csv'
    def open_spider(self,spider):
        if os.path.exists(self.apppath):
            os.remove(self.apppath)
        print(self.apppath)
    def process_item(self, item, spider):
        print(self.apppath)
        with open(self.apppath, 'a', encoding='utf-8') as f:
            f.write( item['ranking']+'\t'
                    +item['movie_name']+'\t'
                    +item['score']+'\t'
                    +item['score_num'] + '\n')

        return item
