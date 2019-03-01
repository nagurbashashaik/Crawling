import scrapy
from scrapy.selector import Selector

class hindu(scrapy.Spider):
        name = "hindu_sample"
        start_urls = ['https://www.thehindu.com/feeder/default.rss']
        data ={}
        def parse(self, response):
            sel = Selector(response)
            sel.remove_namespaces()
            nodes = sel.select('//rss//channel//item')
            for node in nodes:
                title = "".join(node.select('.//title/text()').extract()).strip().encode('utf-8')
                author = "".join(node.select('.//author/text()').extract()).strip().encode('utf-8')
                category = "".join(node.select('.//category/text()').extract()).strip().encode('utf-8')
                link = "".join(node.select('.//link/text()').extract()).strip().encode('utf-8')
                description = "".join(node.select('.//description/text()').extract()).strip().encode('utf-8')
                pubDate = "".join(node.select('.//pubDate/text()').extract()).strip().encode('utf-8')
                print title, author, category, link, description
