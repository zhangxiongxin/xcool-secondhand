from flask import Flask, g
import json
app = Flask(__name__)
def getGoodsList(pageNum, pageSize):
  print(pageNum, pageSize)
  sql = "select * from goods;"
  cursor = g.db.cursor()
  cursor.execute(sql)
  rows = cursor.fetchall()
  result = []
  for row in rows:
    result.append({ 'goodsName': row[4], 'ownerName': row[2], 'currentPrice': row[9], 'originalPrice': row[10], 'goodsImg': row[3] })
  return result