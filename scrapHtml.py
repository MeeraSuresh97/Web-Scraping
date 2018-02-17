import scrapy
class SpiderClass(scrapy.Spider):
    name = "web"
    def __init__(self):
        self.i = 1
    def start_requests(self):
        f = open('filename.txt')
        data = f.read()
        f.close()
        urls = data.split("\n")

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('body'):
            text= quote.css('p').extract()
            f = open('./contentHtml/file'+str(self.i)+'.txt','w')
            f.write(str(text[0]))
            f.close()
            self.i+=1
