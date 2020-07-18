# -*- coding: utf-8 -*-
import json
import random
import time
import traceback
import urllib
import requests

import traceback


import scrapy

from ..items import StatsZbSpiderItem



class StatsDataSpider(scrapy.Spider):
    name = "StatsDataSpider"
    handle_httpstatus_list = [502, 503, 304, 500, 403, 404, 405, 493, 504, 416]

    hgjd_file = "data/zb_hgjd_data.txt"
    hgjd_time = "1978-"
    hgjd_type = 'hgjd'
    hgjd_file_son_zb = "data/zb_hgjd_data_son_zb.txt"
    hgjd_file_son_sj = "data/zb_hgjd_data_son_sj.txt"

    hgyd_file = "data/zb_hgyd_data.txt"
    hgyd_time = "1978-"
    hgyd_type = 'hgyd'
    hgyd_file_son_zb = "data/zb_hgyd_data_son_zb.txt"
    hgyd_file_son_sj = "data/zb_hgyd_data_son_sj.txt"

    hgnd_file = "data/zb_hgnd_data.txt"
    hgnd_time = "1978-"
    hgnd_type = 'hgnd'
    hgnd_file_son_zb = "data/zb_hgnd_data_son_zb.txt"
    hgnd_file_son_sj = "data/zb_hgnd_data_son_sj.txt"


    hg_file = hgnd_file
    hg_time = hgnd_time
    type = hgnd_type
    hg_file_son_zb = hgnd_file_son_zb
    hg_file_son_sj = hgnd_file_son_sj





    download_delay = 8

    allowed_domains = ["data.stats.gov.cn"]
    start_urls = (
        "http://data.stats.gov.cn/easyquery.htm?cn=B01",
    )
    proxy_pool = []

    USER_AGENT_LIST = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 "
        "OPR/26.0.1656.60",
        "Opera/8.0 (Windows NT 5.1; U; en)",
        "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
        "Mozilla/5.0 (Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.11",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 "
        "Safari/534.16",
        "Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/71.0.3578.98 "
        "TaoBrowser/2.0 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.1 "
        "LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR "
        "3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER) ",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR "
        "3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/535.11 SE 2.X "
        "MetaSr 1.0",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE "
        "2.X MetaSr 1.0)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 "
        "Chrome/71.0.3578.98 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 "
        "UBrowser/4.0.3214.0 Safari/537.36",
    ]

    FIRST_PASS = 1
    req_headers = {}

    param = {
        "m": "QueryData",
        "dbcode": type,
        "rowcode": "zb",
        "colcode": "sj",
        "wds": [],
        "k1": "1573266498180"}

    def parse(self, response):
        # self.parse_content(response)
        time.sleep(1)
        with open(self.hg_file, "r") as file:
            zb_list = file.readlines()
        file.close()
        for str in zb_list:
            try:
                str = str.replace("\n","").replace("\'", "\"")
                zb = eval(str)
                if zb['isParent']:
                    print("is parent contine")
                else:
                    self.param["dfwds"] = \
                        json.dumps([{"wdcode": "zb", "valuecode": zb['id']}, {"wdcode": "sj", "valuecode" : self.hg_time}],
                                   separators=(',', ':'))
                    self.req_headers["User-Agent"] = random.choice(self.USER_AGENT_LIST)
                    self.req_headers["Cookie"] = "u=1; __utma=64623162.798167061.1555766737.1555766737.1555766737.1; __utmc=64623162; __utmz=64623162.1555766737.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); JSESSIONID=A77E1A81675F92B04D8033CCBF933F15"
                    request_url = 'http://data.stats.gov.cn/easyquery.htm?' + urllib.parse.urlencode(self.param)
                    print(request_url)
                    res = requests.get(request_url, headers=self.req_headers)
                    self.parse_content(res.json())
                    time.sleep(7)
                    # yield scrapy.Request(url=request_url, method="GET", headers=self.req_headers, dont_filter=True)
            except Exception as e:
                traceback.print_exc()


    def parse_content(self, response):

        try:
            # print(response.text)
            # d = json.loads(response.text)
            # 具体指标
            wdnodes = response['returndata']['wdnodes'][0]['nodes']

            # 具体数据
            datanodes = response['returndata']['datanodes']
            for wdnode in wdnodes:
                item = {}
                item['dbcode'] = self.type
                item['id'] = wdnode['code']
                item['isParent'] = False  # 生成的文件需要将False转换为false,以便下次json.load
                item['name'] = wdnode['cname']
                item['pid'] = wdnode['code'][0:len(wdnode['code']) - 2]
                item['wdcode'] = "zb"
                item['unit'] = wdnode['unit']
                item['exp'] = wdnode['exp']
                print(item)
                with open(self.hg_file_son_zb, "a") as file:
                    file.write(str(item)+"\n")
                file.close()
                dic = {}
                for datastr in datanodes:
                    if datastr['code'].find(item['id']) > 0:
                        dic[datastr['code']] = datastr['data']['data']
                with open(self.hg_file_son_sj, "a") as file2:
                    file2.write(str(dic) + "\n")
                file2.close()
        except Exception as e:
            traceback.print_exc()
            print("parse except")

        # dbcode: "hgnd"
        # id: "A0L01"
        # isParent: false
        # name: "é‡‘èžæœºæž„äººæ°‘å¸ä¿¡è´·èµ„é‡‘å¹³è¡¡è¡¨(èµ„é‡‘æ¥æº)"
        # pid: "A0L"
        # wdcode: "zb"


