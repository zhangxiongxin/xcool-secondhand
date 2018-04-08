from flask import Flask
from flask.ext import restful
from flask import request
from app.api import outApi, user
import json
app = Flask(__name__)
api = restful.Api(app)
class GetCode(restful.Resource):
    def post(self):
        postdata = request.args
        url = 'https://api.miaodiyun.com/20150822/industrySMS/sendSMS'
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        result = outApi.sendPost(url, postdata, headers)
        return result
api.add_resource(GetCode, '/api/getCode')
print(user.generateId())
if __name__ == '__main__':
    app.run(debug=True)