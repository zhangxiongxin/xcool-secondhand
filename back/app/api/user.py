import uuid
from flask import Flask, g
app = Flask(__name__)
def login(userPhone, loginPwd):
  sql = "select * from user where userPhone=%s and loginPwd='%s';" % (userPhone, loginPwd)
  cursor = g.db.cursor()
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
  g.db.commit()
  return {'code': code, 'message': result}
def generateId():
  return uuid.uuid1()