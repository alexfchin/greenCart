#!/usr/bin/python3

from flask import Flask
from flask import request
import pymysql
import sys
import config

app = Flask(__name__)

db_name = config.database_name
db_user = config.database_user
db_password = config.database_password

connection = pymysql.connect(host='127.0.0.1',
                             port=3307,
                             user=db_user,
                             password=db_password,
                             db=db_name)
#sys.exitfunc = connection.close()

def GetEmissions(company):
    #TODO: db stuff
    return 'todo'

@app.route('/company', methods=['GET'])
def GetProductInfo():
    company = request.args.get('company')
    print('Company: {}'.format(company)) #DEBUG
    emissions = GetEmissions(company)
    print('Emissions: {}'.format(emissions)) #DEBUG
    return company

