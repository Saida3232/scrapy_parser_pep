from urllib.parse import urljoin

import scrapy

from pep_parse.constants import PEP_PAGE
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_pages_link = response.css('a::attr(href)').re(r'^pep-\d{1,4}/$')
        for pep_link in pep_pages_link:
            current_link = urljoin(PEP_PAGE, pep_link)
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
