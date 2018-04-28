export function attrChartData () {
  return {
    arrtOption: {
      color: ['#c23531', '#2f4554', '#61a0a8', '#d48265', '#91c7ae', '#749f83', '#ca8622', '#bda29a', '#6e7074', '#546570', '#c4ccd3'],
      title: {
        text: '分类统计',
        subtext: '二手商品分类统计',
        textStyle: {
          color: '#000'
        },
        left: 'center'
      },
      tooltip: {},
      series: [{
        name: '类别',
        type: 'pie',
        selectedMode: 'single',
        selectedOffset: 30,
        clockwise: true,
        label: {
          normal: {
            textStyle: {
              fontSize: 18
            }
          }
        },
        data: [
        ],
        itemStyle: {
          opacity: 0.7,
          borderWidth: 3,
          emphasis: {
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowColor: 'rgba(0, 0, 0, 0.5)'
          }
        }
      }]
    }
  }
}
export function userChartData () {
  return {
    userData: {
      title: {
        text: '注册统计',
        subtext: '注册用户按月统计',
        textStyle: {
          color: '#000'
        },
        left: 'center'
      },
      xAxis: {
        type: 'category'
      },
      yAxis: {
        name: '单位: 人',
        type: 'value'
      },
      dataZoom: [{
        type: 'inside',
        start: 0,
        end: 100
      }, {
        start: 0,
        end: 100
      }],
      series: [{
        type: 'line'
      }]
    }
  }
}
export function buyChartData () {
  return {
    buyData: {
      title: {
        text: '交易统计',
        subtext: '交易量按月统计',
        textStyle: {
          color: '#000'
        },
        left: 'center'
      },
      xAxis: {
        type: 'category'
      },
      yAxis: {
        name: '单位:元',
        type: 'value'
      },
      dataZoom: [{
        type: 'inside',
        start: 0,
        end: 100
      }, {
        start: 0,
        end: 100
      }],
      series: [{
        type: 'bar'
      }]
    }
  }
}
