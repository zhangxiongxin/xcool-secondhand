<template lang="pug">
  .home-index-container
    mHeader
    .home-banner.w
      .brast 发布
      el-carousel.banner(:interval="5000" arrow="always")
        el-carousel-item(v-for="item in 4", :key="item")
          h3 {{ item }}
    .home-list.w
      .recommend 热门推荐
      card(:item="goodsList")
    .home-list.bottom.w
      .recommend 发现低价
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
  .recommend {
    position: relative;
    width: 99%;
    padding-left: 10px;
    font-size: 18px;
    line-height: 30px;
    border-bottom: 1px solid rgba(0, 0, 0, 0.1);
  }
  .recommend::before {
    content: '';
    display: inline-block;
    position: absolute;
    top: 6px;
    left: 0;
    height: 18px;
    width: 4px;
    background: #ffda44;
  }
  .content {
    display: grid;
    grid-template-columns: 35% auto;
    grid-template-rows: auto;
    grid-column-gap: 3rem;
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
    text-align: left;
  }
  .home-list.bottom {
    margin-bottom: 150px;
  }
</style>
