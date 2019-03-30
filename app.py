#!/usr/bin/python3

from flask import Flask
from flask import request
import pymysql
import scrapy
from bs4 import BeautifulSoup
import requests
import sys
import config
#scrapy runspider scraper.py

app = Flask(__name__)

db_name = config.database_name
db_user = config.database_user
db_password = config.database_password

#connection = pymysql.connect(host='127.0.0.1',
#                             port=3307,
#                             user=db_user,
#                             password=db_password,
#                             db=db_name)
#sys.exitfunc = connection.close()

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

#TODO: Added headers
def GetCompany(url):
    SET_SELECTOR = '#bylineInfo'
    page = requests.post(url)
    print(page)
    soup = BeautifulSoup(url, 'html.parser')
    company = soup.find('a', {'id': SET_SELECTOR})
    return company

def GetCompanyEmissions(company):
    #TODO
    return 'todo'

@app.route('/product', methods=['GET'])
def GetProductInfo():
#    GetCompany('banana') #DEBUG
    url = request.args.get('url')
    print('URL: {}'.format(url)) #DEBUG
    company = GetCompany(url)
    print('Company: {}'.format(company)) #DEBUG
#    return GetCompanyEmissions(return)
    return company

