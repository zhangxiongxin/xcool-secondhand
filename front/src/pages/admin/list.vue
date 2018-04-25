<template lang="pug">
  .list-container
    .item(v-for="(item, index) in items", :key="index")
      a {{ item.loginName }}
      a {{ item.userPhone }}
      el-button(@click="controlUser(item.userPhone, 1)") 启用
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
</style>
