import uuid, time, base64, hmac
from flask import Flask, g
app = Flask(__name__)
key = 'xcool95'
def generate_token(key, expire=3600):
    ts_str = str(time.time() + expire)
    ts_byte = ts_str.encode("utf-8")
    sha1_tshexstr  = hmac.new(key.encode("utf-8"),ts_byte,'sha1').hexdigest() 
    token = ts_str+':'+sha1_tshexstr
    b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))
    return b64_token.decode("utf-8")
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
      result = 'success'
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
  sql = "select * from user where userPhone=%s;" % (userPhone)
  cursor = g.db.cursor()
  cursor.execute(sql)
  data = cursor.fetchone()
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
  cursor = g.db.cursor()
  cursor.execute(sql)
  data = cursor.fetchone()
  g.db.commit()
  return data
def generateId():
  return uuid.uuid1()