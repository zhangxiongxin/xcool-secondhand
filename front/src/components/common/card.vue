<template lang="pug">
  .card-container
    .simgle(v-for="(item, index) in item", @click="fun(item)",:key="index")
      img.goodsImg(:src="item.goodsThums")
      a {{ item.goodsName }}
      a ￥ {{ item.currentPrice }}
</template>
<script>
import store from 'store'
export default {
  name: 'card',
  props: {
    item: {
      type: Array,
      required: true
    }
  },
  methods: {
    fun (item) {
      console.dir(item)
      store.set('currentItem', item)
      this.$router.push('/detail')
    }
  }
}
</script>
<style scoped>
  .simgle {
    cursor: pointer;
    display: inline-block;
    width: 10rem;
    height: 14rem;
    margin: 10px 0;
    margin-right: 20px;
  }
  .goodsImg {
    width: 100%;
    height: 80%;
  }
  .card-container {
    display: flex;
    flex-direction: row;
    /*justify-content: space-between;*/
    margin-right: 10px;
    flex-wrap: wrap;
  }
</style>
