# -*- coding :utf-8 -*-


import scrapy
from douban.items import DoubanItem

class Douban_spider(scrapy.Spider):
    name = 'douban'
    login_url='https://movie.douban.com/top250?start=0&filter='
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"}

    base_url = 'https://movie.douban.com/top250?start={}&filter='

    def start_requests(self):
        for i in range(2):
            url = self.base_url.format(i*25)
            yield scrapy.Request(url=url,
                                 headers=self.headers,
                                 callback=self.parse)

    def parse(self, response):
        print(response.url)
        sel  = response.xpath('//div[@class="article"]//ol[@class="grid_view"]/li')
        for li in sel:
            item = DoubanItem()
            item['ranking']= li.xpath('.//div[@class="pic"]/em/text()').extract_first()
            item['movie_name'] = li.xpath('.//div[@class="pic"]//@alt').extract_first()
            item['score'] =li.xpath('.//div[@class="bd"]//div[@class="star"]//span[@class="rating_num"]/text()').extract_first()
            score_num = li.xpath('.//div[@class="bd"]//div[@class="star"]//span/text()').extract()
            item['score_num']='0'
            if score_num is not None:
                score_num=score_num[-1]
                if '人评价' in score_num:
                    score_num = score_num.replace("人评价", "")
                item['score_num'] =score_num
            yield item

