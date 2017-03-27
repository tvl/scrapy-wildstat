# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class WildstatItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Venue(Item):
    country = Field()
    city = Field()
    name = Field()
    opened = Field()
    capacity = Field()
    lat = Field()
    lng = Field()

