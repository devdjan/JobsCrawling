import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from DataCrawler.items import GazpromItem
from datetime import datetime

class GazpromSpider(CrawlSpider):
    name = 'Gazprom'
    allowed_domains = ['gazpromvacancy.ru']
    start_urls = ['https://www.gazpromvacancy.ru/jobs/']

    rules = (
        Rule(LinkExtractor(restrict_css='[class]'), callback='parse_data'),
    )

    def parse_data(self, response):

        items = GazpromItem()

        items['job_url'] = response.url
        items['job_title'] = response.xpath('//div[@class="avia_textblock  "]/p/strong/text()').extract_first(default='not found')
        items['job_description'] = response.xpath('//*[@id="av_section_1"]/div/main/div/div/div[1]/section/div/p[4]//text()').extract()
        items['company_name'] = 'HRForecast'
        items['crawled_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        items['posted_date'] = []

        return items

