import scrapy
from ..items import BluebeamItem
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor


class NhsSpider(scrapy.Spider):
    name = "nhsspider"  # The name of this spider

    # The allowed domain and the URLs where the spider should start crawling:
    allowed_domains = ["www.nhs.uk"]
    start_urls = [
        "https://www.nhs.uk/conditions/"]

    def parse(self, response):
        v = "https://www.nhs.uk"
        for sick in response.css('li.nhsuk-list-panel__item'):
            item = BluebeamItem()
            item["nameDisease"]: sick.css(
                ".nhsuk-list-panel__link::text").extract_first()
            item["urllink"]: v + \
                sick.css(".nhsuk-list-panel__link::attr(href)").extract_first()
            yield item
