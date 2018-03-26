<template lang="pug">
  .home-index-container
    .home-head
      .home-head-left
        a.login(@click="to('/login')") 亲，请登录
        a.register(@click="to('/register')") 免费注册
      upload
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
  .login {
    color: red;
  }
</style>
