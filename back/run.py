from flask import Flask, g
from flask.ext import restful
from flask import request
from app.api import outApi, user, common
from flask.ext.mysql import MySQL
from flask_cors import *
# from flask import make_response
import traceback
import json
mysql = MySQL()
app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'secondhand'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()
api = restful.Api(app)
@app.before_request
def my_before_request():
  g.db = conn
  # print('before request', request.headers)
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
      result = user.login(userPhone)
      return result
api.add_resource(Login, '/api/login')
class QueryUser(restful.Resource):
    def post(self):
      userPhone = request.args.get('userPhone')
      result = user.queryUser(userPhone)
      return result
api.add_resource(QueryUser, '/api/queryUser')
class Register(restful.Resource):
    def post(self):
      userId = request.args.get('userId')
      loginName = request.args.get('loginName')
      userPhone = request.args.get('userPhone')
      alipay = request.args.get('alipay')
      stress = request.args.get('stress')
      result = user.register(userId, loginName, userPhone, alipay, stress)
      return result
api.add_resource(Register, '/api/register')
class GoodsList(restful.Resource):
    def get(self):
      pageNum = request.args.get('pageNum')
      pageSize = request.args.get('pageSize')
      result = common.getGoodsList(pageNum, pageSize)
      return result
api.add_resource(GoodsList, '/api/goodsList')
class AddGoods(restful.Resource):
    def post(self):
      params = request.args
      result = common.addGoods(params)
      return result
api.add_resource(AddGoods, '/api/add')
class QueryUserInfo(restful.Resource):
    def get(self):
      userId = request.args.get('userId')
      result = common.queryUserInfo(userId)
      return result
api.add_resource(QueryUserInfo, '/api/queryUserInfo')
class ModifyUserInfo(restful.Resource):
    def post(self):
      userId = request.args.get('userId')
      alipay = request.args.get('alipay')
      stress = request.args.get('stress')
      loginName = request.args.get('loginName')
      result = user.modify(alipay, loginName, stress, userId)
      return result
api.add_resource(ModifyUserInfo, '/api/modifyUserInfo')
class AdminLogin(restful.Resource):
    def get(self):
      adminId = str(request.args.get('adminId'))
      password = request.args.get('password')
      result = user.adminLogin(adminId, password)
      return result
api.add_resource(AdminLogin, '/api/adminLogin')
class IllegalAccounts(restful.Resource):
    def get(self):
      result = user.illegalAccounts()
      return result
api.add_resource(IllegalAccounts, '/api/illegalAccounts')
class QueryIlUser(restful.Resource):
    def get(self):
      userId = request.args.get('userId')
      result = user.queryIlUser(userId)
      return result
api.add_resource(QueryIlUser, '/api/queryIlUser')
class ControlUser(restful.Resource):
    def post(self):
      userId = request.args.get('userId')
      userStatus = request.args.get('userStatus')
      result = user.controlUser(userId, userStatus)
      return result
api.add_resource(ControlUser, '/api/controlUser')
if __name__ == '__main__':
    app.run(debug=True)
# sql = "select attrCatId count(*) from goods group by attrCatId"