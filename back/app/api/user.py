import uuid, time
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
def queryUser(userPhone):
  sql = "select * from user where userPhone=%s;" % (userPhone)
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
    result = 'no account!'
  g.db.commit()
  return {'code': code, 'message': result}
def register(userId, loginName, loginPwd, userPhone):
  t = time.time()
  userStatus = 1
  sql = "insert into user(userId, loginName, loginPwd, userPhone, userStatus) values ('%s', '%s', '%s', '%s', '%s')" % (userId, loginName, loginPwd, userPhone, userStatus)
  print(sql)
  cursor = g.db.cursor()
  cursor.execute(sql)
  data = cursor.fetchone()
  g.db.commit()
  print(data)
  return data
def generateId():
  return uuid.uuid1()