<template lang="pug">
  .home-index-container
    mHeader
    .home-banner.w
      .brast 发布
      el-carousel.banner(:interval="5000" arrow="always")
        el-carousel-item(v-for="item in 4", :key="item")
          h3 {{ item }}
    .home-list.w
      card(:item="goodsList")
    mFooter
</template>
<script>
export default {
  data () {
    return {
      goodsList: [
        {
          name: '篮球',
          id: 'aaa'
        },
        {
          name: '足球',
          id: 'bbb'
        },
        {
          name: '篮球',
          id: 'aaa'
        },
        {
          name: '足球',
          id: 'bbb'
        },
        {
          name: '篮球',
          id: 'aaa'
        },
        {
          name: '足球',
          id: 'bbb'
        },
        {
          name: '篮球',
          id: 'aaa'
        },
        {
          name: '足球',
          id: 'bbb'
        },
        {
          name: '足球',
          id: 'bbb'
        },
        {
          name: '篮球',
          id: 'aaa'
        },
        {
          name: '足球',
          id: 'bbb'
        },
        {
          name: '篮球',
          id: 'aaa'
        },
        {
          name: '足球',
          id: 'bbb'
        },
        {
          name: '篮球',
          id: 'aaa'
        },
        {
          name: '足球',
          id: 'bbb'
        },
        {
          name: '篮球',
          id: 'aaa'
        },
        {
          name: '足球',
          id: 'bbb'
        },
        {
          name: '篮球',
          id: 'aaa'
        },
        {
          name: '足球',
          id: 'bbb'
        },
        {
          name: '篮球',
          id: 'aaa'
        }
      ]
    }
  },
  methods: {
    to (url) {
      this.$router.push(url)
    }
  }
}
</script>
<style scoped>
  .w {
    max-width: 1200px;
    min-width: 900px;
    margin: 0 auto;
  }
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
    height: 40px;
  }
  .home-logo, .home-bottom {
    height: 90px;
    background: #ffda44;
  }
  .home-bottom {
    width: 100%;
    position: fixed;
    bottom: 0;
    height: 150px;
  }
  .content {
    display: grid;
    grid-template-columns: 35% auto;
    grid-template-rows: auto;
    grid-column-gap: 3rem;
  }
  .name {
    text-align: left;
    font-size: 3rem;
    line-height: 90px;
    position: relative;
  }
  .name-img::after {
    display: inline-block;
    content: '让闲置游荡起来！';
    font-size: .8rem;
    position: absolute;
    top: 0;
    left: 6.5rem;
  }
  .name-slogan {
    font-size: .8rem;
  }
  .item {
    height: 90px;
    line-height: 90px;
    font-size: 1rem;
  }
  .home-banner {
    margin-top: 20px;
    height: 300px;
    display: grid;
    grid-template-columns: 30% auto;
    grid-column-gap: 10px;
  }
  .banner {
    height: 100%;
  }
  .el-carousel__item h3 {
    color: #475669;
    font-size: 18px;
    opacity: 0.75;
    line-height: 300px;
    margin: 0;
  }
  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }
  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
  .brast {
    border: 1px solid #000;
  }
  .home-list {
    margin-top: 20px;
    margin-bottom: 150px;
    text-align: left;
  }
</style>
