<template lang="pug">
  .side-container
    el-menu.el-menu-vertical-demo.left-nav(background-color="#2F4058", active-text-color="#00A0FF", mode="vertical", :router="true", v-for="(item, index) in sideParams", :key="index")
      el-menu-item.left-nav-items(:index="item.sideRoute")
        i(:class="item.sideClass", style="margin-right:5px") {{item.sideName}}
</template>
<script>
export default {
  name: 'side',
  props: ['sideParams'],
  data () {
    return {
      name: 'haha'
    }
  }
}
</script>
<style scoped>
  .left-nav.el-menu {
    border-right: none;
    min-width: 128px;
    width: 128px;
    padding-top: 14px;
  }
  .el-menu .el-menu-item.left-nav-items {
    color: #C0CCDA;
    text-align: left;
    justify-content: left;
    /*padding-left: 10px;*/
    padding-right: 10px;
    width: 128px;
  }
</style>
