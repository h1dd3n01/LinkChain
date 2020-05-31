# LinkChain


Creates a visually representational chained link between a specific website by crawling all of its external link and external links of those external links

**Run**

`scrapy crawl hun7er -a url='your url' -a links='1000'`

`url` is the url you want to crawl.

`links` is the number of links you want to crawl, defaults to 100 if left empty.


`unix4.gv.png` is example result from `json.data` file, scraped **10000** links starting from `https://www.laptopoutlet.co.uk` url

`/spiders/unix4.gv.png` is result from `json.data` file, scraped **100** links starting from `https://www.swappie.com/*` some subdomain
