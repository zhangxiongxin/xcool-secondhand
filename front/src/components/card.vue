<template lang="pug">
  el-row.card-container(:gutter="20")
    el-col.simgle(v-for="(el, index) in item", @click="fun(el.id)",:key="index")
      h1 {{ el.name }}
</template>
<script>
export default {
  name: 'card',
  props: ['item', 'index'],
  methods: {
    fun (id) {
      console.log(id)
    }
  }
}
</script>
<style scoped>
  .simgle {
    float: left;
    width: 10rem;
    height: 14rem;
    border: 1px solid #000;
    padding: 10px;
  }
</style>
