<template lang="pug">
  .register-container
    .words 注册页
    .form(v-if="oneFlag")
      el-input.tel(prefix-icon="el-icon-phone", placeholder="请输入手机号")
      .verification
        el-input.verification-code(prefix-icon="el-icon-view", placeholder="请输入验证码")
          template(slot="append")
            el-button(@click="getVerification") 获取验证码
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
export default {
  data () {
    return {
      oneFlag: true,
      userInfo: {
        name: 'xcool',
        pwd: 'sdfawsd'
      }
    }
  },
  methods: {
    getVerification () {
      console.log('获取验证码')
    },
    register () {
      this.oneFlag = false
    }
  }
}
</script>
<style lang="stylus" scoped>
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
</style>
