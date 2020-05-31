from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from urllib.parse import unquote


class Spider(CrawlSpider):
    name = 'hun73r'
    start_urls = []
    rules = [Rule(LinkExtractor(allow=()), follow=True, callback='parse_data')]
    custom_settings = {
        'DOWNLOAD_DELAY': 1
    }

    def __init__(self, url=None, links=100):
        self.start_urls.append(url)
        self.links = links
        self.counter = 0
        self.link_set = list()
        if url is None:
            raise TypeError('\n[-] Please provide a default url by running \n'
                            '[-] scrapy crawl hun73r -a url="https://someurl.com"')
        super(Spider, self).__init__()

    def parse_data(self, response):
        if self.counter >= int(self.links):
            print('-' * 20)
            # self.rules
            raise CloseSpider("DONE")
        s_link = self.parse_link(response.url)
        deny_url = s_link.split('/')[0]
        for link in LxmlLinkExtractor(allow=(), deny=deny_url).extract_links(response):
            link = self.parse_link(link)
            item = {'original': s_link,
                    'found': link}
            self.link_set.append(item)
            yield item
            self.counter += 1
            print(self.counter)
            if self.counter >= int(self.links):
                print('-' * 20)
                return

    def parse_link(self, inputLink):
        link = unquote(inputLink)
        if link.startswith('https://'):
            link = link.split('//')[1]
        if link.startswith('http://'):
            link = link.split('//')[1]
        if len(link) > 40:
            link = link.split('/')[0]
        return link
