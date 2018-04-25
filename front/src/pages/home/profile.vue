<template lang="pug">
  .profile-container
    mHeader
    el-tabs.tab-container(v-model="activeName", @tab-click="handleClick", :tab-position="tabPosition")
      el-tab-pane(label="个人信息", name="first")
        .userInfo
          .item
            label 支付宝账号
            el-input.normal-input(v-model="alipay", :disabled="writeable")
          .item
            label 创建时间
            label.normal-input {{createTime}}
          .item
            label 昵称
            el-input.normal-input(v-model="loginName", :disabled="writeable")
          .item
            label 手机号码
            label.normal-input {{userPhone}}
          .item
            label 收货地址
            el-input.normal-input(v-model="stress", :disabled="writeable")
          el-button(type="primary", @click="modify") {{btn.value}}
      el-tab-pane(label="订单信息", name="second")
    mFooter
</template>
<script>
import store from 'store'
import CommonService from '@/server/common'
export default {
  name: 'profile',
  data () {
    return {
      tabPosition: 'left',
      activeName: 'first',
      writeable: true,
      alipay: '',
      createTime: '',
      loginName: '',
      stress: '',
      userPhone: '',
      btn: {id: 0, value: '修改'}
    }
  },
  methods: {
    handleClick () {
      console.log('点击tab')
    },
    modify () {
      if (this.btn.id === 0) {
        this.writeable = false
        this.btn = {
          id: 1,
          value: '提交'
        }
      } else {
        console.log('提交')
        let params = {
          alipay: this.alipay,
          loginName: this.loginName,
          stress: this.stress,
          userId: this.userPhone
        }
        CommonService.modifyUserInfo(params)
          .then(() => {
            this.queryUserInfo()
            this.btn = {
              id: 0,
              value: '修改'
            }
            this.writeable = true
          })
          .catch()
      }
    },
    queryUserInfo () {
      let params = {
        userId: store.get('phoneNum')
      }
      CommonService.queryUserInfo(params)
        .then((res) => {
          console.log(res)
          this.alipay = res.message.alipay
          this.createTime = res.message.createTime
          this.loginName = res.message.loginName
          this.stress = res.message.stress
          this.userPhone = res.message.userPhone
        })
        .catch(() => {
          console.log('error in queryUserInfo')
        })
    }
  },
  created () {
    this.queryUserInfo()
  }
}
</script>
<style scoped>
  .userInfo {
    text-align: left;
    width: 600px;
    display: flex;
    flex-direction: column;
    margin: 10px auto 200px auto;
  }
  .normal-input {
    width: 60%;
    float: right;
    margin-bottom: 20px;
  }
  .tab-container {
    max-width: 1200px;
    margin: 0 auto;
  }
</style>
