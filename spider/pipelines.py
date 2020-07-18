# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class StatsSpiderZbPipeline(object):

    def process_item(self, item, spider):
        if spider.name == 'StatsZbHgndSpider':
            with open("data/zb_hgnd_data.txt", "a") as file:
                file.writelines(str(item) + "\n")
            file.close()
        elif spider.name == 'StatsZbHgjdSpider':
            with open("data/zb_hgjd_data.txt", "a") as file:
                file.writelines(str(item) + "\n")
            file.close()
        elif spider.name == 'StatsZbHgydSpider':
            with open("data/zb_hgyd_data.txt", "a") as file:
                file.writelines(str(item) + "\n")
            file.close()
        return item

