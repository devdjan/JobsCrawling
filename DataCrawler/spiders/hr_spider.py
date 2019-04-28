import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from DataCrawler.items import HRforecastsItem
from datetime import datetime

class HRForecastSpider(CrawlSpider):
    name = 'HRForecast'
    allowed_domains = ['hrforecast.de']
    start_urls = ['https://www.hrforecast.de/company/career/']

    rules = (
        Rule(LinkExtractor(restrict_css='[class*=portfolio_grid_career]'), callback='parse_data'),
    )


    def parse_data(self, response):

        items = HRforecastsItem()
        items['job_url'] = response.url
        items['job_title'] = response.xpath('//div[@class="avia_textblock  "]/p/strong/text()').extract_first(default='not found')
        items['job_description'] = response.xpath('//*[@id="av_section_1"]/div/main/div/div/div[1]/section/div/p[4]//text()').extract()
        items['company_name'] = 'HRForecast'
        items['crawled_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        items['posted_date'] = []

        return items
