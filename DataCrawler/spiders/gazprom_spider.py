import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from DataCrawler.items import CrawlersItem
from datetime import datetime

class GazpromSpider(CrawlSpider):
    name = 'Gazprom'
    allowed_domains = ['gazpromvacancy.ru']
    start_urls = ['https://www.gazpromvacancy.ru/jobs/']

    rules = (
        # rule for extracting pagination(.pages) and each job (.job-list-item)
        Rule(LinkExtractor(restrict_css='.pages'), follow=True),
        Rule(LinkExtractor(restrict_css='.job-list-item h3 a'), callback='parse_data')
    )

    def parse_data(self, response):

        items = CrawlersItem()

        items['job_url'] = response.url
        items['job_title'] = response.css('h1.job-title::text').get()
        items['job_description'] = response.css('div.job-info > p::text').getall()
        items['company_name'] = response.css('dl.job-params > dd > a::text').get()
        items['crawled_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # items['posted_date'] = []

        return items

