<template lang="pug">
  .home-index-container
    h1 主页
    ul
      li
        a(@click="to") 登录
</template>
<script>
  export default {
    data() {
      return {

      }
    },
    methods: {
      to () {
        this.$router.push('/login')
      }
    }
  }
</script>
<style scoped>
  ul>li {
    list-style: none;
  }
</style>
