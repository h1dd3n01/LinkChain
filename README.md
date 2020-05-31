# LinkChain


Creates a visually representational chained link between a specific website by crawling all of its external link and external links of those external links

**Run**

`scrapy crawl hun73r -a url='your url' -a links='1000'`

`url` is the url you want to crawl.

`links` is the number of links you want to crawl, defaults to 100 if left empty. By empty i mean you don't input `-a links=''`


`unix4.gv.png` is example result from `data.json` file, scraped **10000** links starting from `https://www.laptopoutlet.co.uk` url

`/spiders/unix4.gv.png` is result from `data2.json` file, scraped **100** links starting from `https://www.swappie.com/*` some subdomain


Data is stored into a `json` file since, if there will be url's with length > 40-50, the render will crash. In case it does, you can always go to the `json` file and remove that long link manually.

Delete the `json`files, rename them or change the output filename in `pipelines.py` , otherwise you'll probably get a `TypeError`
