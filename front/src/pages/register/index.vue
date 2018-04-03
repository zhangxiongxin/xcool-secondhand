<template lang="pug">
  .register-container
    .words 注册页
    .form(v-if="oneFlag")
      el-input.tel(prefix-icon="el-icon-phone", placeholder="请输入手机号")
      .verification
        el-input.verification-code(prefix-icon="el-icon-view", placeholder="请输入验证码")
          template(slot="append")
            el-button.get-code(@click="getVerification", :disabled="timeFlag") {{getCode}}
              a(v-show="timeFlag") s
      el-button.regBtn(@click="register") 注册
    .user-info(v-else)
      h1 请填写必要的信息
      .name
        a 昵称:
        el-input.user-name.user
      .pwd
        a 密码:
        el-input.user-pwd.user(type="password")
      el-button.comfirm 确定
</template>
<script>
import md5 from 'md5'
// import ajax from 'axios'
import ajax from '@/server/ajax'
export default {
  data () {
    return {
      timeFlag: false,
      timer: null,
      getCode: '获取验证码',
      oneFlag: true,
      userInfo: {
        name: 'xcool',
        pwd: 'sdfawsd'
      }
    }
  },
  methods: {
    sendCodeCallback (type, message) {
      this.$message({
        showClose: true,
        message: message,
        type: type
      })
    },
    isTime () {
      clearInterval(this.timer)
      this.timeFlag = false
      this.getCode = '获取验证码'
    },
    getVerification () {
      console.log('获取验证码')
      this.timeFlag = true
      this.getCode = 60
      this.register()
      this.sendCodeCallback('success', '验证码发送成功，请注意查收！')
      this.timer = setInterval(() => {
        this.getCode === 0 ? this.isTime() : this.getCode--
      }, 1000)
    },
    register () {
      // this.oneFlag = false
      var code = 123456
      var m = 5
      // ajax.post('sendSMS', {
      //   accountSid: '26d1714cd0614834a0d62db2c002a730',
      //   to: 17608015960,
      //   timestamp: Date.parse(new Date()),
      //   smsContent: `【惠物品】您的验证码为${code}，请于${m}分钟内正确输入，如非本人操作，请忽略此短信。`,
      //   sig: md5('26d1714cd0614834a0d62db2c002a73055ba8bef73654108b7688c84de9c9ee2' + Date.parse(new Date()))
      // }, {
      //   headers: {'Content-Type': 'application/x-www-form-urlencoded'}
      // })
      var params = {
        accountSid: '26d1714cd0614834a0d62db2c002a730',
        to: 17608015960,
        timestamp: Date.parse(new Date()),
        smsContent: `【惠物品】您的验证码为${code}，请于${m}分钟内正确输入，如非本人操作，请忽略此短信。`,
        sig: md5('26d1714cd0614834a0d62db2c002a73055ba8bef73654108b7688c84de9c9ee2' + Date.parse(new Date()))
      }
      ajax('sendSMS', { method: 'POST', params })
      // ajax.post({
      //   url: '/sendSMS',
      //   methods
      // })
    }
  }
}
</script>
<style lang="stylus" scoped>
  .register-container {
    margin-top 200px
  }
  .form {
    width 400px
    margin 0 auto
    padding 10px
  }
  .verification {
    margin-top 20px
  }
  .regBtn {
    margin-top 20px
    width 100%
  }
  .name, .pwd, comfirm {
    margin-top 20px
  }
  .user {
    width 360px
  }
  .comfirm {
    margin-top 20px
    width 400px
  }
  .get-code {
    width 112px
  }
</style>
