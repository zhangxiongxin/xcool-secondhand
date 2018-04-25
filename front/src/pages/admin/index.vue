<template lang="pug">
  .admin-container
    .login-form(v-if="!hasLogined")
      el-input.input-item(placeholder="请输入管理员账号", v-model="account")
      el-input.input-item(placeholder="请输入管理员密码", type="password", v-model="pwd")
      el-button.input-item(@click="login") 登录
    .content(v-else)
      el-input(placeholder="输入手机号查询用户", v-model="userPhone")
      el-button(type="primary", @click="queryUser") 查询
</template>
<script>
import CommonService from '@/server/common'
import md5 from 'md5'
export default {
  name: 'admin',
  data () {
    return {
      userPhone: '',
      account: '',
      pwd: '',
      hasLogined: false,
      illegalAccountsList: []
    }
  },
  methods: {
    queryUser () {
      let params = {
        userId: this.userPhone
      }
      CommonService.queryIlUser(params)
        .then()
        .catch()
    },
    login () {
      console.log('登录')
      var pwd = `xcool${this.pwd}`
      let params = {
        adminId: this.account,
        password: md5(pwd)
      }
      CommonService.adminLogin(params)
        .then((res) => {
          if (res.result === 'success') {
            console.log('登录成功！')
            this.hasLogined = true
            this.illegalAccounts()
          }
        })
    },
    illegalAccounts () {
      CommonService.illegalAccounts()
        .then((res) => {
          this.illegalAccountsList = res.result
        })
    }
  }
}
</script>
<style scoped>
  .admin-container {
    color: #000;
  }
  .login-form {
    width: 500px;
    height: 300px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    padding: 20px;
  }
  .input-item {
    margin-top: 20px;
  }
</style>
