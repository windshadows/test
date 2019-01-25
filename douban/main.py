
from scrapy import cmdline

cmdline.execute('scrapy crawl douban -o test.csv --nolog'.split())