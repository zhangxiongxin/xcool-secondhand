from flask import Flask
from flask.ext import restful
from flask import request
from app.api import outApi, user
# from flask import make_response
import traceback
import json
app = Flask(__name__)
api = restful.Api(app)
@app.before_request
def my_before_request():
  print('before request', request.headers)
@app.after_request
def my_after_request(self):
  try: print('after request')
  except: traceback.print_exc()
  return self
class GetCode(restful.Resource):
    def post(self):
        # result = make_response()
        postdata = request.args
        url = 'https://api.miaodiyun.com/20150822/industrySMS/sendSMS'
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        result = outApi.sendPost(url, postdata, headers)
        return result
api.add_resource(GetCode, '/api/getCode')
class GetUploadToken(restful.Resource):
    def get(self):
        # print(dir(self))
        key = request.args.get('key')
        print(key)
        token = outApi.getUploadToken(key)
        return { 'token': token }
api.add_resource(GetUploadToken, '/api/getUploadToken')
class Login(restful.Resource):
    def post(self):
      userPhone = request.args.get('userPhone')
      loginPwd = request.args.get('loginPwd')
      result = user.login(userPhone, loginPwd)
      return result
api.add_resource(Login, '/api/login')
print(user.generateId())
if __name__ == '__main__':
    app.run(debug=True)