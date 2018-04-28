import uuid, time, base64, hmac, datetime
from flask import Flask, g
app = Flask(__name__)
key = 'xcool95'
# 生成token
def generate_token(key, expire=3600):
    ts_str = str(time.time() + expire)
    ts_byte = ts_str.encode("utf-8")
    sha1_tshexstr  = hmac.new(key.encode("utf-8"),ts_byte,'sha1').hexdigest() 
    token = ts_str+':'+sha1_tshexstr
    b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))
    return b64_token.decode("utf-8")
# 验证token
def certify_token(key, token):
    token_str = base64.urlsafe_b64decode(token).decode('utf-8')
    token_list = token_str.split(':')
    if len(token_list) != 2:
        return False
    ts_str = token_list[0]
    if float(ts_str) < time.time():
        # token expired
        return 'token expired'
    known_sha1_tsstr = token_list[1]
    sha1 = hmac.new(key.encode("utf-8"),ts_str.encode('utf-8'),'sha1')
    calc_sha1_tsstr = sha1.hexdigest()
    if calc_sha1_tsstr != known_sha1_tsstr:
        # token certification failed
        return 'token certification failed'
    # token certification success
    return True 
def login(userPhone, loginPwd):
  sql = "select loginPwd, userStatus from user where userPhone=%s;" % (userPhone)
  cursor = g.db.cursor()
  cursor.execute(sql)
  data = cursor.fetchone()
  if data:
    code = 10000
    if (data[1] == 1):
      result = { 'name': data[1] }
      token = generate_token(key, 3600)
      return {'code': code, 'message': result, 'token': token}
    else:
      result = 'Account freeze'
  else:
    code = 10001
    result = 'Account or Pwd is error!'
  g.db.commit()
  return {'code': code, 'message': result}
def queryUser(userPhone):
  sql = "select userStatus, loginName from user where userPhone=%s;" % (userPhone)
  cursor = g.db.cursor()
  cursor.execute(sql)
  data = cursor.fetchone()
  code = 10000
  if data:
    if (data[0] == 1):
      result = {'status': 1, 'loginName': data[1]}
      token = generate_token(key, 3600)
      return {'code': code, 'message': result, 'token': token}      
    else:
      result = {'status': 0}
  else:
    result = {'status': 3}
  g.db.commit()
  return {'code': code, 'message': result}
def register(userId, loginName, userPhone, alipay, stress):
  createTime  = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  createNy  = datetime.datetime.now().strftime("%Y.%m")
  sql = "insert into user(userId, loginName, userPhone, alipay, stress, userStatus, createTime, createNy) values ('%s', '%s', '%s', '%s', '%s', 1, '%s', '%s')" % (userId, loginName, userPhone, alipay, stress, createTime, createNy)
  cursor = g.db.cursor()
  cursor.execute(sql)
  data = cursor.fetchone()
  g.db.commit()
  print(data)
  code = 10000
  if (data == None):
      token = generate_token(key, 3600)
      result = 'register success!'
      return {'code': code, 'message': result, 'token': token}
  return {'code': code, 'message': 'fail'}
def modify(alipay, loginName, stress, userId):
  code = 10000
  sql = "update user set alipay='%s', loginName='%s', stress='%s' where userId='%s';" % (alipay, loginName, stress, userId)
  cursor = g.db.cursor()
  cursor.execute(sql)
  data = cursor.fetchone()
  g.db.commit()
  if (data == None):
    sql2 = "update goods set ownerName='%s' where ownerId='%s';" % (loginName, userId)
    sql3 = "update goods_order set ownerName='%s' where ownerId='%s';" % (loginName, userId)
    sql4 = "update goods_order set customerName='%s' where customerId='%s';" % (loginName, userId)
    cursor.execute(sql2)
    cursor.execute(sql3)
    cursor.execute(sql4)
    g.db.commit()
    result = 'modify success!'
    return {'code': code, 'message': result}
  return {'code': code, 'message': 'fail'}
def adminLogin(adminId, password):
  print(adminId, password)
  sql = "select * from admin where adminId='%s';" % (adminId)
  cursor = g.db.cursor()
  cursor.execute(sql)
  data = cursor.fetchone()
  print(data)
  if data:
    if (data[1] == password):
      return {'result': 'success'}
    else:
      return {'result': 'account or password is wrong'}
  else:
    return {'result': 'account or password is wrong'}
def illegalAccounts():
  sql = "select * from user where userStatus=0;"
  cursor = g.db.cursor()
  cursor.execute(sql)
  rows = cursor.fetchall()
  result = []
  for row in rows:
    result.append({ 'loginName': row[1], 'userPhone': row[0] })
  return {'result': result}
def queryIlUser(userId):
  sql = "select * from user where userId='%s';" % (userId)
  cursor = g.db.cursor()
  cursor.execute(sql)
  data = cursor.fetchone()
  if data:
    return { 'loginName': data[1], 'userPhone': data[0], 'userStatus': data[4] }
  return False
def controlUser(userId, userStatus):
  sql = "update user set userStatus='%s' where userId='%s';" % (userStatus, userId)
  cursor = g.db.cursor()
  cursor.execute(sql)
  data = cursor.fetchone()
  g.db.commit()
  if data:
    return True
  return False
def generateId():
  return uuid.uuid1()