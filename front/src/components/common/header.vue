<template lang="pug">
  .home-index-container
    .home-head.w
      .home-head-left
        a.login(@click="to('/login')") 亲，请登录/注册
      .home-head-right
        a.profile(@click="to('/profile')") 个人中心
    .home-logo
      .content.w
        .name
          .name-img 咸鱼
        el-menu.meui(mode="horizontal", background-color="#409EFF", text-color="#eee")
          el-menu-item.item(index="home", @click="to('/')") 首页
          el-menu-item.item(index="it") 数码
          el-menu-item.item(index="cl") 文娱
          el-menu-item.item(index="daily") 服饰
          el-menu-item.item(index="vual") 虚拟
    .home-bottom
</template>
<script>
export default {
  name: 'mHeader',
  data () {
    return {
      name: 'xcool'
    }
  },
  methods: {
    to (url) {
      this.$router.push(url)
      console.log(url)
    }
  }
}
</script>
<style scoped>
  .w {
    max-width: 1200px;
    min-width: 900px;
    margin: 0 auto;
  }
  .home-head-left {
    line-height: 40px;
    font-size: 12px;
    float: left;
    cursor: pointer;
  }
  .login {
    color: red;
    margin-right: 7px;
  }
  .profile {
    float: right;
    line-height: 40px;
    color: #000;
    font-size: 14px;
    cursor: pointer;
  }
  .home-head {
    height: 40px;
  }
  .home-logo, .home-bottom {
    height: 90px;
    background: #409EFF;
  }
  .home-bottom {
    width: 100%;
    position: fixed;
    bottom: 0;
    height: 150px;
  }
  .content {
    display: grid;
    grid-template-columns: 35% auto;
    grid-template-rows: auto;
    grid-column-gap: 3rem;
  }
  .name {
    color: #eee;
    text-align: left;
    font-size: 3rem;
    line-height: 90px;
    position: relative;
  }
  .name-img::after {
    display: inline-block;
    content: '让闲置游荡起来！';
    font-size: .8rem;
    position: absolute;
    top: 0;
    left: 6.5rem;
  }
  .name-slogan {
    font-size: .8rem;
  }
  .item {
    height: 90px;
    line-height: 90px;
    font-size: 1rem;
  }
</style>
