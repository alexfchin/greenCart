#!/usr/bin/python3

from flask import Flask
from flask import request
import pymysql
import scrapy #TODO: Why not beautiful soup?
import sys
import config
#scrapy runspider scraper.py

app = Flask(__name__)

db_name = config.database_name
db_user = config.database_user
db_password = config.database_password

connection = pymysql.connect(host='127.0.0.1',
                             port=3307,
                             user=db_user,
                             password=db_password,
                             db=db_name)
sys.exitfunc = connection.close()

class BrickSetSpider(scrapy.Spider):
    name = 'spider'
    start_urls = []
#    start_urls = ['https://www.amazon.com/dp/B07K7G74P6/ref=br_msw_pdt-4?_encoding=UTF8&smid=AP7ZCPRBBY481&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=&pf_rd_r=N8ND6THGHBZ1AP9HW0VQ&pf_rd_t=36701&pf_rd_p=d8db102a-01f2-4609-b58d-14bd5bbc3e8c&pf_rd_i=desktop']
    def __init__(self, product_url):
        self.start_urls.append(product_url)

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

def GetCompany(product):
    cursor = connection.cursor()
    sql = "SELECT * FROM Brand WHERE Name like %S"
    cursor.execute(sql, (product,))
    result = cursor.fetchone()
    print(result)
    return result

def GetCompanyEmissions(company):
    #TODO
    return 0

@app.route('/product', methods=['GET'])
def GetProductInfo():
    url = request.args.get('url')
    scrape = BrickSetSpider(url)
    
    #DEBUG
    GetCompany('banana')

    #TODO: Where does response come from?
    response = []
    product_name = scrape.parse(response)
    company = GetCompany(product_name)
#    return GetCompanyEmissions(return)
    return company

