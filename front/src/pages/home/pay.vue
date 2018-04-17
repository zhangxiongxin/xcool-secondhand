<template lang="pug">
  .pay-container 付款页面
</template>
<script>
import { uuid } from '@/utils/uuid'
import qs from 'qs'
import md5 from 'md5'
// import CommonService from '@/server/common'
import ajax from 'xe-ajax'
export default {
  name: 'pay',
  data () {
    return {
    }
  },
  methods: {
    pay () {
      var params = {
        appkey: 'aa9119ee467b44599f700bdfe1293740',
        method: 'trpay.trade.create.scan',
        timestamp: Date.parse(new Date()) / 1000,
        version: '1.0',
        outTradeNo: uuid(),
        payType: 1,
        tradeName: 'ball',
        amount: '10',
        notifyUr: 'http://208.167.255.15:5000',
        payuserid: uuid()
      }
      const objKeySort = (obj) => {
        var newkey = Object.keys(obj).sort()
        var newObj = {}
        for (var i = 0; i < newkey.length; i++) {
          newObj[newkey[i]] = obj[newkey[i]]
        }
        return newObj
      }
      // let AppSecret = 'fd9c7b11db2d42778100774159a9d9db'
      console.dir(objKeySort(params))
      // console.log(qs.stringify(params))
      var stringSignTemp = `${qs.stringify(params)}&AppSecret=fd9c7b11db2d42778100774159a9d9db`
      let sign = md5(stringSignTemp).toUpperCase()
      params.sign = sign
      // CommonService.pay(params)
      //   .then(res => {
      //     console.log(res)
      //   })
      //   .catch(err => {
      //     console.log(err)
      //   })
      ajax.fetch(`order/trpayGetWay?${qs.stringify(params)}`, {
        method: 'POST'
      }).then((res) => {
        console.log(res)
      }).catch()
    }
  },
  created () {
    this.pay()
  }
}
</script>
<style scoped>
</style>
