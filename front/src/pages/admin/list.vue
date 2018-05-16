<template lang="pug">
  .list-container
    h3 禁用用户
    .item(v-for="(item, index) in items", :key="index")
      a.nick-name 昵称：{{ item.loginName }}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      a.phone 电话：{{ item.userPhone }}
      //- el-button(@click="controlUser(item.userPhone, 1)") 启用
      a.qy(@click="controlUser(item.userPhone, 1)") 启用
</template>
<script>
export default {
  name: 'list',
  data () {
    return {
      name: 'xcool'
    }
  },
  props: {
    items: {
      type: Array,
      required: true
    }
  },
  methods: {
    controlUser (userId, type) {
      this.$emit('controlUser', userId, type)
    }
  }
}
</script>
<style scoped>
  .item {
    margin-top: 10px;
    /*margin-bottom: 10px;*/
  }
  .qy {
    color: #409EFF;
    display: inline-block;
    margin-left: 10px;
  }
  .nick-name {
    display: inline-block;
    width: 200px;
    text-align: left;
  }
  .phone {
    display: inline-block;
    width: 200px;
    text-align: left;
  }
</style>
