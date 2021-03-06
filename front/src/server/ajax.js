// import store from 'store'
import axios from 'axios'
function replaceParams (url, params) {
  return (url + ' ').replace(/:(.*?)(\/|\?| )/g, function (a, b, c) {
    let tmp = params[b]
    delete params[b]
    return tmp + c
  }).trim()
}
var serverHost = process.env.NODE_ENV !== 'development' ? 'http://127.0.0.1:5000' : ''
export default function xhr (path, options = {}) {
  var config = Object.assign({
    url: serverHost + replaceParams(path, options.params),
    method: options.method,
    data: options.body,
    headers: Object.assign({
      'Content-Type': 'application/x-www-form-urlencoded'
    }, options.headers)
  }, options)
  return new Promise((resolve, reject) => {
    axios(config).then(resp => {
      resolve(resp.data)
    }).catch(err => { console.log(err) })
  })
}
