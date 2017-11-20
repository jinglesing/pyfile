import scrapy

class DmozSpider(scrapy.Spider):
    name = "my"
    allowed_domains = ["taptap.com"]
    start_urls = [
        "https://www.taptap.com/search/apps?kw=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80",
        
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]+".html"
        with open(filename, 'wb') as f:
            f.write(response.body)