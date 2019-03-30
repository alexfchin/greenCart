import scrapy
#scrapy runspider scraper.py

class BrickSetSpider(scrapy.Spider):
    name = 'spider'
    start_urls = ['https://www.amazon.com/dp/B07K7G74P6/ref=br_msw_pdt-4?_encoding=UTF8&smid=AP7ZCPRBBY481&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=&pf_rd_r=N8ND6THGHBZ1AP9HW0VQ&pf_rd_t=36701&pf_rd_p=d8db102a-01f2-4609-b58d-14bd5bbc3e8c&pf_rd_i=desktop']
    def parse(self, response):
        byinfoName = ''
        SET_SELECTOR = '#bylineInfo'
        for tag in response.css(SET_SELECTOR):
            NAME_SELECTOR = 'a ::text'
            yield {
                'name': tag.css(NAME_SELECTOR).extract_first(),
            }
            byinfoName += tag.css(NAME_SELECTOR).extract_first()
        print(byinfoName.capitalize())
        return byinfoName


