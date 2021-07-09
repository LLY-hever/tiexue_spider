# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeaponItem(scrapy.Item):
    # define the fields for your item here like:

    #Name = scrapy.Field()

    Source = scrapy.Field()

    Title = scrapy.Field()

    Website = scrapy.Field()

    Date = scrapy.Field()

    Content = scrapy.Field()

    Keyword = scrapy.Field()

    pass