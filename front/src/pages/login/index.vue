<template lang="pug">
  .login-container
    h1 登录页
    el-input(placeholder="请输入手机号", v-model="phoneNum")
    el-input(type="password", placeholder="请输入密码", v-model="pwd")
    el-button(@click="login") 登录
</template>
<script>
import CommonService from '@/server/common'
import md5 from 'md5'
export default {
  data () {
    return {
      phoneNum: 17608015960,
      pwd: 123456
    }
  },
  methods: {
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
    }
  },
  created () {
    this.login()
  }
}
</script>
<style scoped>
</style>
