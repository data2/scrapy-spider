
from scrapy import cmdline

# cmdline.execute('scrapy crawl StatsZbHgndSpider'.split(' '))
# cmdline.execute('scrapy crawl StatsZbHgjdSpider'.split(' '))
# cmdline.execute('scrapy crawl StatsZbHgydSpider'.split(' '))

cmdline.execute('scrapy crawl StatsDataSpider'.split(' '))
