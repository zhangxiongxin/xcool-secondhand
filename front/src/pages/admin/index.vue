<template lang="pug">
  .admin-container
    .login-form(v-if="!hasLogined")
      el-input.input-item(placeholder="请输入管理员账号", v-model="account")
      el-input.input-item(placeholder="请输入管理员密码", type="password", v-model="pwd")
      el-button.input-item(@click="login") 登录
</template>
<script>
export default {
  name: 'admin',
  data () {
    return {
      account: '',
      pwd: '',
      hasLogined: false
    }
  },
  methods: {
    login () {
      console.log('登录')
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
