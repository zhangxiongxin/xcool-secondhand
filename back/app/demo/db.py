from flask import Flask
from flask.ext.mysql import MySQL
mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'secondhand'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
def dbHand(userPhone, loginPwd):
  cursor = mysql.connect().cursor()
  sql = "SELECT * from User where userPhone=" + userPhone + " and loginPwd='" + loginPwd + ";"
  cursor.execute(sql)
  data = cursor.fetchall()
  mysql.connect().commit()
  mysql.connect().close()
  return data
