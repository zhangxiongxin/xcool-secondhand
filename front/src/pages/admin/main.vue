<template lang="pug">
  .main-container
    side.side(:sideParams="sideData")
    .content
      .attr(ref="attr")
      .user(ref="user")
      .buy(ref="buy")
</template>
<script>
import { attrChartData, userChartData, buyChartData } from './data'
import side from './side'
import echarts from 'echarts'
export default {
  name: 'emain',
  components: { side },
  data () {
    return {
      name: 'emain',
      sideData: [{
        sideRoute: ``,
        sideClass: 'el-icon-setting',
        sideName: '用户管理'
      }, {
        sideRoute: ``,
        sideClass: 'el-icon-info',
        sideName: '统计数据'
      }],
      attrList: [
        {
          value: '12',
          name: '数码'
        },
        {
          value: '15',
          name: '文娱'
        },
        {
          value: '87',
          name: '服饰'
        },
        {
          value: '21',
          name: '虚拟'
        },
        {
          value: '54',
          name: '其他'
        }
      ]
    }
  },
  methods: {
    init () {
      let attrChart = this.$refs.attr
      this.attrChart = echarts.init(attrChart)
      var data = attrChartData().arrtOption
      data.series[0].data = this.attrList
      this.attrChart.setOption(data)
      //  aja
      let userChart = this.$refs.user
      this.userChart = echarts.init(userChart)
      var userData = userChartData().userData
      userData.xAxis.data = ['2018.01', '2018.02', '2018.03', '2018.04', '2018.06', '2018.07', '2018.08', '2018.09', '2018.10', '2018.11', '2018.12']
      userData.series[0].data = [40, 50, 60, 70, 50, 60, 20, 12, 56, 78, 10]
      this.userChart.setOption(userData)
      // buy
      let buyChart = this.$refs.buy
      this.buyChart = echarts.init(buyChart)
      var buyData = buyChartData().buyData
      buyData.xAxis.data = ['2018.01', '2018.02', '2018.03', '2018.04', '2018.06', '2018.07', '2018.08', '2018.09', '2018.10', '2018.11', '2018.12']
      buyData.series[0].data = [40, 50, 60, 70, 50, 60, 20, 12, 56, 78, 10]
      this.buyChart.setOption(buyData)
    }
  },
  mounted () {
    this.init()
  }
}
</script>
<style scoped>
  .attr, .user, .buy {
    margin: 40px;
    width: 900px;
    height: 600px;
  }
  .side {
    height: 100vh;
    background: #2F4058;
  }
  .main-container {
    height: 100%;
    display: flex;
  }
  .content {
    padding: 20px;
    height: 100vh;
    display: flex;
  }
</style>
