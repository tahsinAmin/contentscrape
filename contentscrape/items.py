# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ContentscrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    image_link = scrapy.Field()
    price = scrapy.Field()
    review = scrapy.Field()
    amenities = scrapy.Field()
    location = scrapy.Field()