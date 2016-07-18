# -*- coding: utf-8 -*-
from __future__ import absolute_import
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.loader.processors import TakeFirst
from scrapy.loader import XPathItemLoader
from scrapy.selector import HtmlXPathSelector
from markov_spider.items import MarkovSpiderItem
import markov_spider.items
import scrapy
import os.path





class LinkinParkSpider(CrawlSpider):

    name = "Linkin"
    allowed_domains = ["songlyrics.com/"]
    start_urls = ["http://www.songlyrics.com/linkin-park-lyrics/"]


    def parse(self, response):
        links = []
        Items = items.MarkovSpiderItem()
        Items[link] = response.xpath('//div[@class="listbox"]//table[@class="tracklist"]/tbody//tr//td//a/@href').extract()
        for href in response.xpath('//div[@class="listbox"]//table[@class="tracklist"]/tbody//tr//td//a/@href'):
            url = response.urljoin(href.extract())
            links.append(href.extract())
            print "Start"
            yield scrapy.Request(url, callback=self.parse_content)
            print "End"
        # for link in links:
        #     print link

    def parse_content(self, response):
        print "Im on "+response.url
        LItems = items.MarkovSpiderItem()
        LItems[title] = response.xpath('//div[@class="pagetitle"]/h1.text()').extract()
        LItems[lyric] = response.xpath('//p[@id="songLyricsDiv"]/text()').extract()

        fileName="././Lyrics/Linkin_Park"
        fileName = os.path.join(file.name, LItems[title])
        file = open("fileName", 'w')
        file.write(LItems[lyric])
        file.close()
