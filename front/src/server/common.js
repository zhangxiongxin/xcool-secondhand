import xhr from './ajax'
class CommonService {
  getUploadToken (params) {
    return xhr('api/getUploadToken', { method: 'GET', params })
  }
  pay (params) {
    return xhr('order/trpayGetWay', { method: 'GET', params })
  }
}
export default new CommonService()
