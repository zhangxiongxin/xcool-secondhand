import requests
import json
def sendGet(self):
  r = requests.get(self)
  return json.loads(r.text)
def sendPost(url, data, headers):
  r = requests.post(url, data, headers)
  return json.loads(r.text)
