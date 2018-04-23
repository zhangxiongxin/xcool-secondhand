<template lang="pug">
  .detail-container
    mHeader
    .content.w(v-if="noPay")
      .content-left
        img.goodsImg(:src="imgSrc")
      .content-right
        .name {{ goodsName }}
        .currentPrice
          a.label-price 价格
          sub.symbol ￥
          a.price-num {{ currentPrice }}
        .originalPrice
          a.label-price 原价
          a.origin-price-num {{ originalPrice }}
        .ownerName {{ ownerName }}
        el-button(@click="pay", type="primary") 立即购买
    .pay-container.w(e-else)
      .logo 收银台
      .order-info
        .order-num 132123
        .order-type 数码
        .order-money ￥78.40
      .qr-container
        .img-container
          img.wx_logo(src="/static/img/wx_logo.png")
        .img-container
          img.wx_qr(src="/static/img/qr.png")
        .img-container
          img.wx_intro(src="/static/img/intro.png")
    mFooter
</template>
<script>
import store from 'store'
export default {
  name: 'detail',
  data () {
    return {
      noPay: true,
      imgSrc: store.get('currentItem').goodsImg,
      goodsName: store.get('currentItem').goodsName,
      currentPrice: store.get('currentItem').currentPrice,
      originalPrice: store.get('currentItem').originalPrice,
      ownerName: store.get('currentItem').ownerName
    }
  },
  methods: {
    pay () {
      this.noPay = false
      setTimeout(() => {
        this.noPay = true
      }, 5000)
    }
  },
  created () {
  }
}
</script>
<style scoped>
  .w {
    max-width: 1200px;
    min-width: 900px;
    margin: 0 auto;
  }
  .content, .pay-container {
    margin-bottom: 250px;
    height: 600px;
    display: flex;
    align-items: center;
  }
  .pay-container {
    flex-direction: column;
  }
  .content-left {
    width: 450px;
    height: 300px;
    border: 1px solid #000;
    margin-right: 15px; 
  }
  .goodsImg {
    max-height: 100%;
    max-width: 100%;
  }
  .name {
    font-size: 16px;
    color: #000;
    font-weight: 700;
    line-height: 1.5;
    padding-bottom: .2em;
  }
  .origin-price-num {
    text-decoration: line-through;
  }
  .content-right {
    width: 450px;
    height: 300px;
    border: 1px solid #000;
  }
  .symbol {
    color: #FF0036;
    font-size: 15px;
  }
  .price-num {
    color: #FF0036;
    font-size: 30px;
  }
  .wx_logo {
    width: 20px;
  }
  .wx_qr {
    width: 200px;
    height: 200px;
  }
  .wx_intro {
    width: 200px;
    height: 60px;
  }
</style>
