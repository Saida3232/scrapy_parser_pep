from urllib.parse import urljoin

import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import ALLOWED_DOMAINS, PEP_SPIDER_NAME, START_URLS


class PepSpider(scrapy.Spider):
    name = PEP_SPIDER_NAME
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URLS

    def parse(self, response):
        pep_pages_link = response.css('a::attr(href)').re(r'^pep-\d{1,4}/$')
        for pep_link in pep_pages_link:
            current_link = urljoin(self.start_urls[0], pep_link)
            yield response.follow(current_link, callback=self.parse_pep)

    def parse_pep(self, response):
        status = response.css('dt:contains("Status"), dd:contains("Status")')
        next_dd_text = status.xpath('following-sibling::dd[1]//text()').get()
        data = {
            'number': response.css('h1.page-title::text').get().split()[1],
            'name': response.css('h1.page-title::text').get(),
            'status': next_dd_text
        }
        yield PepParseItem(data)
