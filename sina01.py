# -*- coding: utf-8 -*-

from ..items import Sina01Item
import scrapy

class sina01Spider(scrapy.Spider):
    name = 'sina01'
    start_urls = ['http://sports.sina.com.cn/basketball/nba/2017-04-01/doc-ifycwyns4168962.shtml']

    def parse(self, response):
        sports = Sina01Item()
        print (response)
        title = response.xpath(".//*[@id='j_title']/text()").extract()[0].encode("utf-8")
        content = response.xpath(".//*[@id='artibody']/p/text()").extract()[0].encode("utf-8")
        time = response.xpath(".//*[@class='layout-wrap-a layout-pt-b layout-mt-c clearfix']/div[2]/div[1]/article/div[1]/span[1]/text()").extract()[0].encode("utf-8")
        #print title
       # print time
       # print content




        sports ['title'] = title
        sports['time'] = time
        sports['content'] = content

        yield sports




