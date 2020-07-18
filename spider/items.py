# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StatsZbSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    dbcode = scrapy.Field()
    id = scrapy.Field()
    isParent = scrapy.Field()
    name = scrapy.Field()
    pid = scrapy.Field()
    wdcode = scrapy.Field()




