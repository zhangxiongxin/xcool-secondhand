<template lang="pug">
  .create-container
    mHeader
    .upload-container
      input.upload-input(type="file", @change="update")
      button(@click="preUpload") 开始上传
    mFooter
</template>
<script>
import CommonService from '@/server/common'
const region = 'http://up.qiniu.com'
export default {
  name: 'createItem',
  data () {
    return {
      name: 'xcool',
      file: null,
      key: '',
      token: ''
    }
  },
  methods: {
    // 上传前通过服务端获取七牛云上传凭证
    preUpload () {
      CommonService.getUploadToken({ key: this.key })
        .then(res => {
          console.log(res)
          this.token = res.token
          this.upload(this.file, this.token, this.key)
        })
        .catch(err => {
          console.log(err)
        })
    },
    upload (f, token, key) {
      var xhr = new XMLHttpRequest()
      xhr.open('POST', region, true)
      var formData
      formData = new FormData()
      formData.append('key', key)
      formData.append('token', token)
      formData.append('file', f)
      xhr.onreadystatechange = (res) => {
        if (xhr.readyState === 4 && xhr.status === 200 && xhr.responseText !== '') {
          var result = JSON.parse(xhr.responseText)
          console.log(result)
        }
      }
      xhr.send(formData)
    },
    update (e) {
      let file = e.target.files[0]
      console.log(file)
      this.file = file
      this.key = file.name
    }
  },
  created () {
  }
}
</script>
<style scoped>
  .upload-container {
    margin-top: 40px;
  }
  .upload-input {
    /*opacity: 0;*/
  }
</style>
