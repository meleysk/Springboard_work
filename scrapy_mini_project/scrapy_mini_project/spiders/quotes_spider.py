import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]
    # This method does the same thing. we dont have to implement it and can use the sortcut above
    # declare the urls as attributes. This happens because parse() is the default call back and will
    # be called regardless

    # def start_requests(self):
    #     urls = [
    #         'http://quotes.toscrape.com/page/1/',
    #         'http://quotes.toscrape.com/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
        # check next page, if there is call parse method on it
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
            # next_page = response.urljoin(next_page)
            # yield scrapy.Request(next_page, callback=self.parse)

    # # Parse method using xpath scraper
    # def parse_xpath(self, response):
    #     for quote in response.xpath('//div//*[@class="quote"]'):
    #          yield {
    #             'text': quote.xpath('.//span[contains(concat(" ",normalize-space(@class)," ")," text ")]//text()').get()
    #             'author':quote.xpath('.//small[contains(concat(" ",normalize-space(@class)," ")," author ")]//text()').get()
    #             'tag': quote.xpath('.//div[contains(concat(" ",normalize-space(@class)," ")," tags ")]//a[contains(concat(" ",normalize-space(@class)," ")," tag ")]//text()').getall()
    #         }
    # #next_page = response.css('li.next a::attr(href)').get()
    # next_page = response.xpath('.//li[@class and contains(concat(" ", normalize-space(@class), " "), " next ")]//a/@href').get()
