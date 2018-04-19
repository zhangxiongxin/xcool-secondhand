from flask import Flask, g
import json
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