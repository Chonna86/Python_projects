import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com']

    def __init__(self, *args, **kwargs):
        super(QuotesSpider, self).__init__(*args, **kwargs)
        self.authors = []  # Додайте список для збереження даних про авторів

    def parse(self, response):
        for quote in response.css('div.quote'):
            author = quote.css('small.author::text').get()
            quote_data = {
                'author': author,
                'quote': quote.css('span.text::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
            self.authors.append({'fullname': author})  # Додайте дані про автора до списку

            yield quote_data

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def closed(self, reason):
        # Збереження даних про авторів у файл authors.json
        with open('authors.json', 'w') as f:
            json.dump(self.authors, f, indent=2)