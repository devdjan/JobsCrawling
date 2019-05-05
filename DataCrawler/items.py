# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CrawlersItem(scrapy.Item):
    job_url = scrapy.Field()
    job_title = scrapy.Field()
    job_description = scrapy.Field()
    company_name = scrapy.Field()
    crawled_date = scrapy.Field()
    posted_date = scrapy.Field()



