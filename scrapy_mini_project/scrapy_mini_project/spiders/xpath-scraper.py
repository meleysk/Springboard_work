# spider using xpath selectors

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "xpath-scraper"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.xpath('//div//*[@class="quote"]'):
            yield {
                'text': quote.xpath('.//span[contains(concat(" ",normalize-space(@class)," ")," text ")]//text()').get(),
                'author': quote.xpath('.//small[contains(concat(" ",normalize-space(@class)," ")," author ")]//text()').get(),
                'tag': quote.xpath('.//div[contains(concat(" ",normalize-space(@class)," ")," tags ")]//a[contains(concat(" ",normalize-space(@class)," ")," tag ")]//text()').getall()
            }

        next_page = response.xpath(
            './/li[@class and contains(concat(" ", normalize-space(@class), " "), " next ")]//a/@href').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
