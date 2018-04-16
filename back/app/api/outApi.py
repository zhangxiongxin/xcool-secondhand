import requests
import json
from qiniu import Auth
AccessKey = '7uWRD62toYPbRB3YU9iRXJqbkAB6h1j-xocU0EV-'
SecretKey = 'dh5kSun9W0IP3zYj6tzfNAHmYxIbbSsJ15UAfwul'
bucket_name = 'xcool-secondhand'
delay = 3600
def sendGet(self):
  r = requests.get(self)
  return json.loads(r.text)
def sendPost(url, data, headers):
  r = requests.post(url, data, headers)
  return json.loads(r.text)
def getUploadToken(self):
  q = Auth(AccessKey, SecretKey)
  token = q.upload_token(bucket_name, self, delay)
  return token
