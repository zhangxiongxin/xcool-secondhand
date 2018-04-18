import uuid
from flask import Flask
from flask.ext.mysql import MySQL
mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'secondhand'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
def login(userPhone, loginPwd):
  cursor = mysql.connect().cursor()
  sql = "select * from user where userPhone=%s and loginPwd='%s';" % (userPhone, loginPwd)
  print(sql)
  cursor.execute(sql)
  data = cursor.fetchone()
  print(data)
  if data:
    code = 10000
    if (data[5] == 1):
      result = 'success'
    else:
      result = 'Account freeze'
  else:
    code = 10001
    result = 'Account or Pwd is error!'
  mysql.connect().commit()
  mysql.connect().close()
  return {'code': code, 'message': result}
def generateId():
  return uuid.uuid1()