from flask import Flask, g
import json, uuid, time
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
    result.append({ 'goodsId': row[0], 'goodsName': row[4], 'ownerName': row[2], 'currentPrice': row[9], 'originalPrice': row[10], 'goodsImg': row[3] })
  return result
def addGoods(params):
  goodsId = uuid.uuid1()
  ownerId = params.ownerId
  ownerName = params.ownerName
  goodsName = params.goodsName
  attrCatId = params.attrCatId
  currentPrice = params.currentPrice
  createTime = time.time()
  isSale = 0
  goodsImg = params.goodsImg
  goodsDesc = params.goodsDesc 
  originalPrice = params.originalPrice
  goodsThums = params.goodsThums
  sql = "insert into goods values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);" % (goodsId, ownerId, ownerName, goodsImg, goodsName, isSale, goodsDesc, attrCatId, createTime, currentPrice, originalPrice, goodsThums)
  cursor = g.db.cursor()
  cursor.execute(sql)
  rows = cursor.fetchall()
  if rows[0] == 'null':
    return { 'code': 10000, 'message': 'success' }