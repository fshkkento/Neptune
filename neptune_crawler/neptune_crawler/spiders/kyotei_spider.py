import scrapy


class KyoteiSpider(scrapy.Spider):
    name = "kyotei"

    def start_requests(self):
        urls = [
            'https://kyotei.sakura.ne.jp/kako-20201212.html',
            'https://kyotei.sakura.ne.jp/kako-20201211.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
