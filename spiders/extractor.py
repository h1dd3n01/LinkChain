from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider


class Spider(CrawlSpider):
    name = 'hun73r'
    start_urls = []
    rules = [Rule(LinkExtractor(allow=()), follow=True, callback='parse_data')]
    custom_settings = {
        'DOWNLOAD_DELAY': 5
    }

    def __init__(self, url=None, links=100):
        self.start_urls.append(url)
        self.links = links
        self.counter = 0
        if url is None:
            raise TypeError('\n[-] Please provide a default url by running \n'
                            '[-] scrapy crawl hun73r -a url="https://someurl.com"')
        super(Spider, self).__init__()

    def parse_start_url(self, response):
        if self.counter >= int(self.links):
            print('-' * 20)
            raise CloseSpider("DONE")
        while self.counter <= int(self.links):
            s_link = response.url.split('//')[1].split('/')[0]

            for link in LxmlLinkExtractor(allow=(), deny=()).extract_links(response):
                yield {'original': s_link,
                       'found': link.url}
                self.counter += 1
                print(self.counter)
                if self.counter >= int(self.links):
                    print('-' * 20)
                    raise CloseSpider("DONE")
                # print(self.counter)
