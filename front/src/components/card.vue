<template lang="pug">
  .card-container
    .simgle(v-for="(item, index) in item", @click="fun(item)",:key="index")
      img.goodsImg(src="https://img.alicdn.com/bao/uploaded/i1/2354695424/TB28ckgayqAXuNjy1XdXXaYcVXa_!!2354695424.jpg_200x200.jpg")
      h3 名称: {{ item.name }}
      //- h3 id: {{ item.id }}
</template>
<script>
export default {
  name: 'card',
  props: ['item', 'index'],
  methods: {
    fun (item) {
      console.log(item.id)
    }
  }
}
</script>
<style scoped>
  .card-container {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: space-between;
  }
  .simgle {
    display: inline-block;
    width: 10rem;
    height: 14rem;
    margin: 10px;
  }
  .goodsImg {
    width: 100%;
    height: 80%;
  }
</style>
