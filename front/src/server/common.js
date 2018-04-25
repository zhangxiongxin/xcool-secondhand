import xhr from './ajax'
class CommonService {
  getUploadToken (params) {
    return xhr('api/getUploadToken', { method: 'GET', params })
  }
  addItem (params) {
    return xhr('api/add', { method: 'POST', params })
  }
  login (params) {
    return xhr('api/login', { method: 'POST', params })
  }
  queryUser (params) {
    return xhr('api/queryUser', { method: 'POST', params })
  }
  queryUserInfo (params) {
    return xhr('api/queryUserInfo', { method: 'GET', params })
  }
  modifyUserInfo (params) {
    return xhr('api/modifyUserInfo', { method: 'POST', params })
  }
  register (params) {
    return xhr('api/register', { method: 'POST', params })
  }
  pay (params) {
    return xhr('order/trpayGetWay', { method: 'GET', params })
  }
  goodsList (params) {
    return xhr('api/goodsList', { method: 'GET', params })
  }
  adminLogin (params) {
    return xhr('api/adminLogin', { method: 'GET', params })
  }
  illegalAccounts () {
    return xhr('api/illegalAccounts', { method: 'GET' })
  }
  queryIlUser (params) {
    return xhr('api/queryIlUser', { method: 'GET', params })
  }
}
export default new CommonService()
