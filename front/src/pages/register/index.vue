<template lang="pug">
  .register-container
    .words 注册页
    .form(v-if="oneFlag")
      el-input.tel(prefix-icon="el-icon-phone", placeholder="请输入手机号", v-model="phoneNum")
      .verification
        el-input.verification-code(prefix-icon="el-icon-view", placeholder="请输入验证码", v-model="authCode")
          template(slot="append")
            el-button.get-code(@click="getVerification", :disabled="timeFlag") {{getCode}}
              a(v-show="timeFlag") s
      el-button.regBtn(@click="register") 下一步
    .user-info(v-else)
      h1 请填写必要的信息
      .name
        a 昵称:
        el-input.user-name.user(v-model="loginName")
      .pwd
        a 密码:
        el-input.user-pwd.user(type="password", v-model="loginPwd")
      el-button.comfirm(@click="comfirm") 注册
</template>
<script>
import md5 from 'md5'
// import ajax from 'axios'
import CommonService from '@/server/common'
import store from 'store'
import ajax from '@/server/ajax'
export default {
  data () {
    return {
      authCode: null,
      phoneNum: '',
      timeFlag: false,
      timer: null,
      getCode: '获取验证码',
      oneFlag: true,
      userInfo: {
        name: 'xcool',
        pwd: 'sdfawsd'
      },
      loginName: '',
      loginPwd: ''
    }
  },
  methods: {
    random () {
      var num = ''
      for (let i = 0; i < 6; i++) {
        num += Math.floor(Math.random() * 10)
      }
      console.log(num)
      return num
    },
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
      var code = this.random()
      var m = 5
      var params = {
        accountSid: '26d1714cd0614834a0d62db2c002a730',
        to: this.phoneNum,
        timestamp: Date.parse(new Date()),
        smsContent: `【惠物品】您的验证码为${code}，请于${m}分钟内正确输入，如非本人操作，请忽略此短信。`,
        sig: md5('26d1714cd0614834a0d62db2c002a73055ba8bef73654108b7688c84de9c9ee2' + Date.parse(new Date()))
      }
      var pwd = md5(`${code}${this.phoneNum}xcool`)
      console.log(pwd, 11)
      store.set('pwd', pwd)
      ajax('api/getCode', { method: 'POST', params })
        .then(res => {
          this.timeFlag = true
          this.getCode = 60
          this.sendCodeCallback('success', '验证码发送成功，请注意查收！')
          setTimeout(() => {
            store.remove('pwd')
          }, 30000)
          this.timer = setInterval(() => {
            this.getCode === 0 ? this.isTime() : this.getCode--
          }, 1000)
        })
    },
    register () {
      var pwd = md5(`${Number(this.authCode)}${this.phoneNum}xcool`)
      console.log(pwd, 22, store.get('pwd'))
      if (pwd !== store.get('pwd')) {
        console.log('认证成功！')
        let params = {
          userPhone: this.phoneNum
        }
        CommonService.queryUser(params)
          .then(res => {
            console.log(res)
            if (res.code === 10001) {
              this.oneFlag = false
            }
          })
          .catch(() => {
            this.oneFlag = false
          })
      }
    },
    auth (str) {
      if (str.length > 5 && str.length < 16) return true
      return false
    },
    comfirm () {
      if (!this.auth(this.loginName) || !this.auth(this.loginPwd)) {
        this.sendCodeCallback('error', '请正确填写昵称和密码后再进行提交')
      } else {
        let params = {
          userId: this.phoneNum,
          loginName: this.loginName,
          loginPwd: md5(this.loginPwd),
          userPhone: this.phoneNum
        }
        CommonService.register(params)
          .then(() => {
            console.log('ss')
          })
          .catch()
      }
    }
  },
  destoryed () {
    this.timer = null
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
