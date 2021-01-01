# -*- coding: utf-8 -*-
import re
import scrapy
from ..items import AmazontutorialItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [ 'https://www.amazon.com/dp/B07PY359Q8']
    def Find(string):  # findall() has been used  # with valid conditions for urls in string
        return url
    def parse(self, response):
        items = AmazontutorialItem()

        product_name =response.css('#productTitle::text').extract()
        product_price =  response.css('#priceblock_ourprice::text').extract()
        product_des = response.css('#feature-bullets .a-list-item::text').extract()

        product_imagelink = response.xpath('//li/span/span/div[@class="imgTagWrapper"]/img/@data-a-dynamic-image').get()
        product_des = [x.replace('\n', '').replace('\t', '') for x in product_des]
        items['product_name'] =''.join(product_name).strip()
        items['product_price'] = product_price[0]
        items['product_des'] = ''.join(product_des).strip()
        print("ergr",product_price)
        st=""
        qw=product_imagelink.split(",\"")
        links=[]
        print("qwerty",qw[0])
        for i in range(0,len(qw)):
            qw[i]=qw[i].split(":[")[0]

        qw[0]=qw[0][1:]
        qw[len(qw)-1]=qw[len(qw)-1][:-1]
        print(qw)
        items['product_imagelink'] = qw
        yield items

