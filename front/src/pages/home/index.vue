<template lang="pug">
  .home-index-container
    .home-head
      .home-head-left
        a.login(@click="to('/login')") 亲，请登录
        a.register(@click="to('/register')") 免费注册
      //- upload
    .home-logo
    .home-banner
    .home-list
    .home-bottom
</template>
<script>
import upload from '../../components/upload'
export default {
  data () {
    return {

    }
  },
  components: {
    upload: upload
  },
  methods: {
    to (url) {
      this.$router.push(url)
    }
  }
}
</script>
<style scoped>
  .home-head-left {
    line-height: 40px;
    font-size: 12px;
    float: left;
  }
  .login {
    color: red;
    margin-right: 7px;
  }
  .home-head {
    max-width: 1200px;
    height: 40px;
    margin: 0 auto;
  }
  .home-logo {
    height: 90px;
    background: #ffda44;
  }
</style>
