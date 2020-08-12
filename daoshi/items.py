# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DaoshiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    school_id = scrapy.Field()
    email = scrapy.Field()
    title = scrapy.Field()
    phone = scrapy.Field()
    tutor_id = scrapy.Field()
    clicks = scrapy.Field()
    name = scrapy.Field()
    yes_rank = scrapy.Field()
    aspect = scrapy.Field()
    special = scrapy.Field()
    school = scrapy.Field()
    depart = scrapy.Field()
    introduce = scrapy.Field()
    work = scrapy.Field()
    pass
