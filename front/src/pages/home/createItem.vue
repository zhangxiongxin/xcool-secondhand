<template lang="pug">
  .create-container
    mHeader
    .upload-container
      el-button.upload-container(type="primary")
        span.upload-btn 上传
          input.upload-input(type="file", @change="update", multiple="multiple", ref="uploadForm")
      img.goods-img(:src="imgSrc")
      el-button(@click="preUpload") 开始上传
      //- el-upload.uploader(action="", :show-file-list="false", :on-success="update", :before-upload="update", :auto-upload="false", :on-preview="update")
      //-   img.goods-img(v-if="imgSrc", :src="imgSrc")
      //-   i.el-icon-plus.uploader-img(v-else)
    mFooter
</template>
<script>
import CommonService from '@/server/common'
import { uuid } from '@/utils/uuid'
const region = 'http://up.qiniu.com'
// const Imgurl = 'http://opma82b7e.bkt.clouddn.com'
export default {
  name: 'createItem',
  data () {
    return {
      name: 'xcool',
      file: null,
      key: '',
      token: '',
      fileType: '',
      uploadList: [],
      imgSrc: ''
    }
  },
  methods: {
    // 上传前通过服务端获取七牛云上传凭证
    preUpload () {
      if (!this.file) throw new Error('file in empty!')
      CommonService.getUploadToken({ key: this.key })
        .then(res => {
          // console.log(res)
          this.token = res.token
          this.upload(this.file, this.token, this.key)
        })
        .catch(() => {
          // console.log(err)
        })
    },
    // 七牛云上传图片接口
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
          console.log(result, '上传图片返回')
        } else {
          // console.log(res, '上传失败')
        }
      }
      xhr.send(formData)
    },
    // 本地图片上传
    update (e) {
      let file = e.target.files[0]
      console.log(file)
      this.file = file
      switch (file.type) {
        case 'image/x-icon':
          this.fileType = `.icon`
          break
        case 'image/png':
          this.fileType = `.png`
          break
        default:
          this.fileType = `.jpg`
      }
      let src = URL.createObjectURL(file)
      console.log(src)
      this.imgSrc = src
      var fileName = uuid()
      this.key = `${fileName}${this.fileType}`
      console.dir(this.$refs.uploadForm)
    }
  },
  created () {
    // console.log(uuid())
  }
}
</script>
<style scoped>
  .upload-container {
    margin-top: 40px;
  }
  .upload-input {
    position:absolute;
    right: 0px;
    top:0px;
/*    opacity: 0;
    -ms-filter: 'alpha(opacity=0)';*/
    font-size: 200px;
  }
  .goods-img {
    max-width: 600px;
  }
  .upload-btn {

  }
  .upload-container {
    position: relative;
    display: inline-block;
    overflow: hidden;
  }
/*  .uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
    width: 600px;
    height: 600px;
  }
  .uploader .el-upload:hover {
    border-color: #409EFF;
  }
  .uploader-img {
    border: 1px dashed #d9d9d9;
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  }
  .goods-img {
    width: 178px;
    height: 178px;
    display: block;
  }*/
</style>
