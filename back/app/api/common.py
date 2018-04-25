from flask import Flask, g
import json, uuid, time, datetime, re
app = Flask(__name__)
def getGoodsList(pageNum, pageSize):
  pageNum = int(pageNum)
  pageSize = int(pageSize)
  start = pageSize * (pageNum - 1)
  sql = "select * from goods limit %s, %s;" % (start, pageSize)
  cursor = g.db.cursor()
  cursor.execute(sql)
  rows = cursor.fetchall()
  result = []
  for row in rows:
    result.append({ 'goodsId': row[0], 'ownerId': row[1], 'goodsName': row[4], 'ownerName': row[2], 'currentPrice': row[9], 'originalPrice': row[10], 'goodsImg': row[3], 'goodsThums': row[11] })
  return result
def queryUserInfo(userId):
  sql = "select * from user where userId='%s'" % (userId)
  cursor = g.db.cursor()
  cursor.execute(sql)
  rows = cursor.fetchone()
  createTime = format(rows[5])
  result = {'loginName': rows[1],'userPhone': rows[2],'createTime': createTime,'alipay': rows[6],'stress': rows[7]}
  return {'code': 10000, 'message': result}
def addGoods(params):
  myUuid = str(uuid.uuid1())
  print(myUuid)
  goodsId = re.sub(r'-', "", myUuid)
  ownerId = params.get('ownerId')
  ownerName = params.get('ownerName')
  goodsName = params.get('goodsName')
  attrCatId = params.get('attrCatId')
  currentPrice = params.get('currentPrice')
  createTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  isSale = 0
  goodsImg = params.get('goodsImg')
  goodsDesc = params.get('goodsDesc' )
  originalPrice = params.get('originalPrice')
  goodsThums = params.get('goodsThums')
  sql = "insert into goods values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (goodsId, ownerId, ownerName, goodsImg, goodsName, isSale, goodsDesc, attrCatId, createTime, currentPrice, originalPrice, goodsThums)
  print(sql)
  cursor = g.db.cursor()
  cursor.execute(sql)
  rows = cursor.fetchone()
  g.db.commit()
  if rows == None:
    return { 'code': 10000, 'message': 'success' }
  else:
    return { 'code': 10000, 'message': 'fail' }