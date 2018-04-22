<template lang="pug">
  .login-container
    .login-top
      a(@click="to('/')") 首页
    .login-center
      .content.w
        .center-left
          img.bg(src="/static/img/login_bg.png")
        .center-right(v-if="oneFlag")
          label.tips 账号登录/注册
          el-input(prefix-icon="el-icon-phone", placeholder="请输入手机号", v-model="phoneNum")
          .verification
            el-input.verification-code(prefix-icon="el-icon-view", placeholder="请输入验证码", v-model="authCode")
              template(slot="append")
                el-button.get-code(:type="btnType", @click="getVerification", :disabled="timeFlag") {{getCode}}
                  a(v-show="timeFlag") s
          el-button.login_btn(type="primary", @click="register") 登录/注册
        .user-info(v-else)
          h4 请填写必要的信息
          .name
            a.reg-info 昵称:
            el-input.user-name.user(v-model="loginName")
          .pwd
            a.reg-info 支付宝账号:
            el-input.user-pwd.user(v-model="zfb")
          .stress
            a.reg-info 详细地址:
            el-input.stress-in(type="textarea", v-model="stress", :rows="2", resize="none")
          el-button.comfirm(type="primary", @click="comfirm") 确定
    .login-bottom
</template>
<script>
import CommonService from '@/server/common'
import md5 from 'md5'
import store from 'store'
import ajax from '@/server/ajax'
export default {
  data () {
    return {
      zfb: '',
      phoneNum: '',
      getCode: '获取验证码',
      btnType: 'primary',
      authCode: null,
      timeFlag: false,
      timer: null,
      oneFlag: true,
      userInfo: {
        name: 'xcool',
        pwd: 'sdfawsd'
      },
      loginName: '',
      loginPwd: '',
      stress: ''
    }
  },
  methods: {
    to (url) {
      this.$router.push(url)
    },
    login () {
      let params = {
        userPhone: this.phoneNum,
        loginPwd: md5(this.pwd)
      }
      CommonService.login(params)
        .then(res => {
          this.$router.push('/')
        })
        .catch(err => { console.log(err) })
    },
    // 获取验证码
    getVerification () {
      var code = this.random()
      console.log(typeof code, code)
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
    // 生成六位数随机码
    random () {
      var num = ''
      for (let i = 0; i < 6; i++) {
        num += Math.floor(Math.random() * 10)
      }
      console.log(num)
      return num
    },
    // alert封装
    sendCodeCallback (type, message) {
      this.$message({
        showClose: true,
        message: message,
        type: type
      })
    },
    // 计时器
    isTime () {
      clearInterval(this.timer)
      this.timeFlag = false
      this.getCode = '获取验证码'
    },
    // 简单验证输入
    auth (str) {
      if (str.length > 5 && str.length < 16) return true
      return false
    },
    // 新注册用户填写资料提交验证
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
    },
    register () {
      /*
        流程：
          1.验证码校验；
          2.检测账号是否存在；
            2.1 账号存在 > 进入首页
            2.2 账号不存在 > 下一步
          3.填写个人信息 > 进入首页
      */
      console.log(typeof this.authCode, this.authCode)
      var pwd = md5(`${this.authCode}${this.phoneNum}xcool`)
      console.log(pwd, 22, store.get('pwd'))
      if (pwd === store.get('pwd')) {
        console.log('认证成功！')
        let params = {
          userPhone: this.phoneNum
        }
        CommonService.queryUser(params)
          .then(res => {
            console.log(res)
            if (res.message.status === 1) {
              this.to('/')
            } else if (res.message.status === 3) {
              this.sendCodeCallback('error', '该账号被冻结，请与管理员连写')
            } else {
              this.oneFlag = false
            }
          })
          .catch(() => {
            this.sendCodeCallback('error', '系统错误')
          })
      } else {
        this.sendCodeCallback('error', '验证码错误！')
      }
    }
  },
  created () {
    // this.login()
  },
  destoryed () {
    this.timer = null
  }
}
</script>
<style scoped>
  .w {
    height: 100%;
    max-width: 1200px;
    margin: 0 auto;
    position: relative;
  }
  .login-top {
    height: 150px;
  }
  .login-center {
    padding: 0 10%;
    background: #009ce4;
    height: 600px;
  }
  .content {
    display: flex;
    flex-direction: row;
    align-items: center;
  }
  .center-left {
    width: 40%;
    margin-right: 15%;
  }
  .bg {
    max-width: 100%;
    max-height: 100%;
  }
  .center-right{
    padding: 20px;
    position: relative;
    width: 360px;
    height: 260px;
    background: #ecf9ff;
    display: flex;
    flex-direction: column;
  }
  .login-bottom {
    height: 150px;
  }
  .verification, .login_btn {
    margin-top: 20px;
  }
  .get-code {
    width: 112px;
  }
  .tips {
    font-size: 19px;
    font-weight: 600;
    text-align: left;
    line-height: 3;
  }
  .user-info {
    padding: 20px;
    position: relative;
    width: 400px;
    height: 260px;
    background: #ecf9ff;
    display: flex;
    flex-direction: column;
  }
  .name, .stress, .pwd {
    display: flex;
    flex-direction: row;
    margin-top: 10px;
  }
  .reg-info {
    width: 35%;
    text-align: left;
    line-height: 40px;
  }
  .comfirm {
    margin-top: 20px;
  }
</style>
