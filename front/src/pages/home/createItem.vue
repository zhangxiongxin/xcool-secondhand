<template lang="pug">
  .create-container
    mHeader
    .upload-container
      input(type="file")
    mFooter
</template>
<script>
export default {
  name: 'createItem',
  data () {
    return {
      name: 'xcool'
    }
  },
  created () {
    console.log('add')
  }
}
</script>
<style scoped>
  .upload-container {
    margin-top: 40px;
  }
</style>
