import scrapy

from scrapy.loader import ItemLoader
from ..items import NbrmmkItem
from itemloaders.processors import TakeFirst


class NbrmmkSpider(scrapy.Spider):
	name = 'nbrmmk'
	start_urls = ['http://www.nbrm.mk/']

	def parse(self, response):
		post_links = response.xpath('//div[@class="news-articles-wrapper"]/article')
		for post in post_links:
			title = post.xpath('./div[@class="news-intro-title"]/h2/text()').get()
			description = ''
			date = post.xpath('./p[@class="date-publishing"]/text()').get()

			item = ItemLoader(item=NbrmmkItem(), response=response)
			item.default_output_processor = TakeFirst()
			item.add_value('title', title)
			item.add_value('description', description)
			item.add_value('date', date)

			yield item.load_item()
