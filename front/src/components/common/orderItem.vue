<template lang="pug">
  .orderItem-container
    .content(v-for="(item, index) in items", :key="index")
      a {{ item.goodsName }}
</template>
<script>
export default {
  name: 'orderItem',
  props: {
    items: {
      type: Array,
      required: true
    },
    type: {
      type: String,
      required: true
    }
  },
  data () {
    return {
      name: 'orderItem'
    }
  }
}
</script>
<style scoped>
  .orderItem-container {
    color: #000;
  }
</style>
