# -*- coding: utf-8 -*-
import scrapy
from wildstat.items import Venue

class VenuesSpider(scrapy.Spider):
    name = "venues"
    allowed_domains = ["wildstat.com"]
    start_urls = ['http://wildstat.com/map_stadium/']

    def start_requests(self):
        for i in range(1,9603):
            yield scrapy.Request(url=self.start_urls[0]+str(i), callback=self.parse)


    def parse(self, response):
        venue = Venue()
        venue['country'], venue['city'], venue['name'] = response.css('title::text')[0].extract().split(',')
        res = response.xpath('//td//b/text()')
        if len(res) > 0:
            venue['opened'] = res[0].extract()
        res = response.xpath('//td//b/text()')
        if len(res) > 1:
            venue['capacity'] = res[1].extract()
        venue['lat'], venue['lng'] = response.xpath('//script/text()')[1].re(r'\((.*)\)')[1].split(',')
        return venue
