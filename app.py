# -*- coding=utf-8
from flask import Flask, request
from detect_rec_plate import main_handler
import json

app = Flask(__name__)

@app.route('/event-invoke', methods = ['POST', 'GET'])
def invoke():
    path = "imgs"
    event = {"dictionary" : path}
    context = None
    array = main_handler(event, context)
    result = ''
    for item in array:
        result += '车牌号为：' + item + '\n'
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)

