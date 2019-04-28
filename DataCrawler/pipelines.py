# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2

class DatacrawlerPipeline(object):

    def open_spider(self, spider):
        hostname = 'localhost'
        username = 'manager'  # the username when you create the database
        password = 'hrforecast'  # change to your password
        database = 'jobs_hrforecast'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cur.execute("insert into jobs_data(job_url, job_title, job_description, company_name, crawled_date, posted_date) values(%s,%s,%s,%s,%s,%s)", (item['job_url'], item['job_title'], item['job_description'], item['company_name'], item['crawled_date'], item['posted_date']))
        self.connection.commit()
        return item