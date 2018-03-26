from flask import Flask
from flask.ext import restful
from flask.ext.mysql import MySQL
from flask import request
from flask import make_response
import os
import json
mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'demo'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
app = Flask(__name__)
api = restful.Api(app)
@app.route("/Authenticate")
def Authenticate():
    # username = request.args.get('UserName')
    # password = request.args.get('Password')
    # cursor = mysql.connect().cursor()
    # cursor.execute("SELECT * from User where Username='" + username + "' and Password='" + password + "'")
    data = "sdfs"
    if data is None:
     return "Username or Password is wrong"
    else:
     return "Logged in successfully"
class HelloWorld(restful.Resource):
    def get(self):
        return {
          'data': 10103,
          'code': {
            'a': 1,
            'b': 2
          }
        }
    def post(self):
      cursor = mysql.connect()
      # result2 = dir(mysql.connect())
      # result = dir(cursor)
      sql = "select * from User;"
      sql2 = 'INSERT into User VALUES (4566646,"xcool","asxaxa");'
      (cursor.cursor()).execute(sql2)
      # data = (cursor.cursor()).fetchall()
      cursor.commit()
      cursor.close()
      return "haha"
class Upload(restful.Resource):
    def post(self):
        response = make_response()
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST'
        response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type' 
        f = request.files['file']
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        target = "static//uploads"
        upload_path = os.path.join(basepath,target,f.filename) #注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
        return response
api.add_resource(HelloWorld, '/api')
api.add_resource(Upload, '/upload')
# api.add_resource(HelloWorld, '/api')
if __name__ == '__main__':
    app.run(debug=True)