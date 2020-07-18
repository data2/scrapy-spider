# -*- coding: utf-8 -*-
import json
import time
import urllib

import scrapy
from user_agent import generate_user_agent

from ..items import StatsZbSpiderItem


class StatsZbHgjdSpider(scrapy.Spider):
    name = 'StatsZbHgjdSpider'
    allowed_domains = ['data.stats.gov.cn']
    start_urls = ['http://data.stats.gov.cn/easyquery.htm?cn=C01']

    DOWNLOAD_DELAY =20

    get_tree_url = 'http://data.stats.gov.cn/easyquery.htm'

    root_zb = ['A01', 'A02', 'A03', 'A04', 'A05', 'A06']
    # root_zb = ['A01']

    root_param ={"dbcode":"hgjd","wdcode":"zb","m":"getTree"}

    user_agent = generate_user_agent()
    headers = {
    'Accept': 'text/plain, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    # 'Content-Length': '38',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'JSESSIONID=F57026E9795D5E42B04115AB1FC3F258; u=1; wzws_cid=7043b0f11490d1af13890c46dab3c77ff11815b0d6ed6e0bb208fba85822ed47ea9b8783a325b98ef76e90cfe4933255c2f6c6ab8c95edff8fd3105126e023a7',
    'Host': 'data.stats.gov.cn',
    'Origin': 'http://data.stats.gov.cn',
    'Referer': 'http://data.stats.gov.cn/easyquery.htm',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'}
    headers["User-Agent"]=user_agent

    def parse(self, response):
        for id in self.root_zb:
            self.root_param["id"] = id
            yield scrapy.FormRequest(url=(self.get_tree_url+"?"+urllib.parse.urlencode(self.root_param)),method='POST',headers=self.headers,callback=self.parse_content,dont_filter=True)
            # yield scrapy.FormRequest(url=self.get_tree_url, method='POST',
            #                          headers=self.headers,callback=self.parse_content,dont_filter=True)

    def parse_content(self, response):
        try:
            time.sleep(1)
            if 200 != response.status:
                print("res status not 200!")
            # print(str(response.body,"utf-8"))
            son_zb_arr = json.loads(str(response.body,"utf-8"))
            for key in son_zb_arr:
                # item = StatsZbSpiderItem()
                # item['dbcode'] = key['dbcode']
                # item['id'] = key['id']
                # item['isParent'] = key['isParent']
                # item['name'] = key['name']
                # item['pid'] = key['pid']
                # item['wdcode'] = key['wdcode']
                # print(key)
                if key['isParent']:
                    self.root_param["id"] = key["id"]
                    yield scrapy.FormRequest(url=(self.get_tree_url + "?" + urllib.parse.urlencode(self.root_param)),
                                             method='POST', headers=self.headers, callback=self.parse_content,
                                             dont_filter=True)
                yield key
        except BaseException:
            print('')
