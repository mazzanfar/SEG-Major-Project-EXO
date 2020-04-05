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
            nameOfDisease = sick.css(
                ".nhsuk-list-panel__link::text").extract_first()
            link = v + \
                sick.css(".nhsuk-list-panel__link::attr(href)").extract_first()
            item["nameDisease"] = nameOfDisease
            item["urllink"] = link
            yield item

            #next_url = response.css('').get()
