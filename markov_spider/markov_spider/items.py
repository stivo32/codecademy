# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MarkovSpiderItem(scrapy.Item):
    title = scrapy.Field()
    lyric = scrapy.Field()

class LinkinItem(scrapy.Item):
    link = scrapy.Field()

