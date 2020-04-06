import scrapy
from ..items import BluebeamItem
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor


class SuperSpider(scrapy.Spider):
    name = "superspider"  # The name of this spider

    # The allowed domain and the URLs where the spider should start crawling:
    allowed_domains = ["www.disability-grants.org"]
    start_urls = [
        "https://www.disability-grants.org/"]

    def parse(self, response):
        for sick in response.xpath(''):
            item = BluebeamItem()
            nameOfDisease = sick.xpath(
                "//a/text()").extract_first()
            link = sick.css("//a/@href").extract_first()
            item["nameDisease"] = nameOfDisease
            item["urllink"] = link
            yield item

            #next_url = response.css('').get()
