<template lang="pug">
    .login-form(v-if="!hasLogined")
      el-input.input-item(placeholder="请输入管理员账号", v-model="account")
      el-input.input-item(placeholder="请输入管理员密码", type="password", v-model="pwd")
      el-button.input-item(@click="login") 登录
    .content(v-else)
      .query-container
        .top
          el-input.query_user(placeholder="输入手机号查询用户", v-model="userPhone")
          el-button.query_btn(type="primary", @click="queryUser") 查询
        h3 查询结果
        .bottom
          label.nick-name 昵称：{{queryResult.loginName}}
          label.phone-num 手机号：{{queryResult.userPhone}}
          el-button(@click="controlUser(queryResult.userPhone, 0)", type="primary") 禁用
          //- a.jy 禁用
      list.my-list(:items="illegalAccountsList", @controlUser="controlUser")
</template>
<script>
import CommonService from '@/server/common'
import md5 from 'md5'
import list from './list'
export default {
  name: 'adminLogin',
  components: {
    list: list
  },
  data () {
    return {
      userPhone: '',
      account: '',
      pwd: '',
      hasLogined: false,
      illegalAccountsList: [],
      queryResult: {
        loginName: '',
        userPhone: ''
      }
    }
  },
  methods: {
    controlUser (id, type) {
      let params = {
        userId: id,
        userStatus: type
      }
      CommonService.controlUser(params)
        .then((res) => {
          console.log(res)
          this.illegalAccounts()
        })
    },
    queryUser () {
      let params = {
        userId: this.userPhone
      }
      CommonService.queryIlUser(params)
        .then((res) => {
          this.queryResult.loginName = res.loginName
          this.queryResult.userPhone = res.userPhone
        })
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
  .content {
    display: flex;
    width: 1400px;
    margin: 0 auto;
    margin-top: 200px;
  }
  .query-container {
    border: 1px solid #ccc;
    display: flex;
    width: 600px;
    flex-direction: column;
    padding: 40px;
    border-radius: 5px;
    margin-right: 60px;
  }
  .query_user {
    width: 70%;
    margin-right: 5%;
  }
  .query_btn {
    width: 25%;
  }
  .my-list {
    border: 1px solid #ccc;
    display: flex;
    width: 600px;
    flex-direction: column;
    border-radius: 5px;
  }
  .nick-name {
    text-align: left;
    display: inline-block;
    margin-right: 20px;
  }
  .phone-num {
    text-align: left;
    display: inline-block;
    margin-right: 20px;
  }
  .bottom {
    margin-top: 20px;
    text-align: left;
  }
  .jy {
    color: #409EFF;
  }
</style>
