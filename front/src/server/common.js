import xhr from './ajax'
class CommonService {
  getUploadToken (params) {
    return xhr('api/getUploadToken', { method: 'GET', params })
  }
  login (params) {
    return xhr('api/login', { method: 'POST', params })
  }
  pay (params) {
    return xhr('order/trpayGetWay', { method: 'GET', params })
  }
}
export default new CommonService()
