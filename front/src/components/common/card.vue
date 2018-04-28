<template lang="pug">
  .card-container
    .simgle(v-for="(item, index) in item", @click="fun(item)",:key="index")
      img.goodsImg(:src="item.goodsThums")
      a {{ item.goodsName }}
      a.money ￥{{ item.currentPrice }}
    .add(@click="add")
      p.icon-circle +
      p 加载更多
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
    },
    add () {
      this.$emit('add')
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
  .money {
    color: red;
  }
  .add {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    font-size: 13px;
    color: #999999;
    cursor: pointer;
    width: 10rem;
    height: 14rem;
    margin: 10px 0;
    margin-right: 20px;
  }
  .add .icon-circle {
    width: 33px;
    height: 33px;
    margin-bottom: 10px;
    background-color: #00A0FF;
    border-radius: 50%;
    text-align: center;
    font-size: 36px;
    line-height: 33px;
    color: #FFFFFF;
  }
</style>
