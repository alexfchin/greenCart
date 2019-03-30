#!/usr/bin/python3

from flask import Flask
from flask import request
from flask import jsonify
import pymysql
import config

app = Flask(__name__)

db_name = config.database_name
db_user = config.database_user
db_password = config.database_password

connection = pymysql.connect(host='127.0.0.1',
                             port=3307,
                             user=db_user,
                             password=db_password,
                             db=db_name,
                             cursorclass=pymysql.cursors.DictCursor)

def GetEmissions(company):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM Company WHERE Name LIKE %s"
            cursor.execute(sql, [company])
            result = cursor.fetchone()
            return result
    except Exception as ex:
        print("Error: {}".format(ex))
        return ex
    finally:
        cursor.close()

@app.route('/company', methods=['GET'])
def GetProductInfo():
    company = request.args.get('company')
    print('Company: {}'.format(company)) #DEBUG
    emissions = GetEmissions(company)
    print('Emissions: {}'.format(emissions)) #DEBUG
    if emissions is None:
        error = {
                'error': 404,
                'message': 'Company not found'
                }
        return jsonify(error)
    else:
        return jsonify(emissions)

