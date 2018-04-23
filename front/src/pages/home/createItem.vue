<template lang="pug">
  .create-container
    mHeader
    .upload-container.w
      .child.goods-name-container
        .label.required 商品名
        el-input.input-right(placeholder="请输入商品名", v-model="form.goodsName")
      .child.price-container
        .label.required 商品价格
        el-input.input-right(placeholder="请输入商品价格", v-model="form.currentPrice")
      .child.origin-container
        .label 商品原价
        el-input.input-right(placeholder="请输入商品原价", v-model="form.originalPrice")
      .child.classify-container
        .label.required 商品分类
        el-select.input-right(v-model="form.attrCatId")
          el-option(v-for="item in options", :key="item.value", :label="item.label", :value="item.value")
      .child.goods-desc-container
        .label 描述
        el-input.input-right.desc(type="textarea", v-model="form.goodsDesc", :rows="4", resize="none", placeholder="请输入对商品的一些描述")
      .goods-img-container
        el-button.uploadbtn-container(type="primary")
          span.upload-btn 上传图片
            input.upload-input(type="file", @change="update", multiple="multiple", ref="uploadForm")
        img.goods-img(:src="imgSrc")
      .goods-btn-container
        el-button.brast(@click="preUpload", type="primary") 发布闲置
        el-button.cancel(@click="cancel") 取消
    mFooter
</template>
<script>
import CommonService from '@/server/common'
import { uuid } from '@/utils/uuid'
import store from 'store'
const region = 'http://up.qiniu.com'
const ImgBaseUrl = 'http://p79ebonvg.bkt.clouddn.com'
export default {
  name: 'createItem',
  data () {
    return {
      form: {
        ownerId: store.get('phoneNum'),
        ownerName: store.get('loginName'),
        attrCatId: '',
        goodsImg: '',
        goodsName: '',
        goodsDesc: '',
        currentPrice: '',
        originalPrice: '',
        goodsThums: ''
      },
      options: [{
        value: 0,
        label: '数码'
      }, {
        value: 1,
        label: '文娱'
      }, {
        value: 2,
        label: '服饰'
      }, {
        value: 3,
        label: '虚拟'
      }, {
        value: 4,
        label: '其他'
      }],
      name: 'xcool',
      file: null,
      key: '',
      token: '',
      fileType: '',
      uploadList: [],
      imgSrc: '',
      imgUrl: '',
      imgThumb: ''
    }
  },
  methods: {
    to (url) {
      this.$router.push(url)
    },
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
          this.form.goodsImg = `${ImgBaseUrl}/${result.key}`
          this.form.goodsThums = `${ImgBaseUrl}/${result.key}/thumb`
          this.commitItem()
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
    },
    // 提交表单，上传商品
    commitItem () {
      CommonService.addItem(this.form)
        .then((res) => {
          console.log(res)
          this.to('/')
        })
        .catch((err) => {
          console.log(err)
        })
    },
    cancel () {
      this.to('/')
    }
  },
  created () {
    // console.log(uuid())
  }
}
</script>
<style scoped>
  .required {
    position: relative;
  }
  .required::before {
    font-size: 16px;
    content: "*";
    display: inline-block;
    position: absolute;
    color: red;
    left: -21px;
    top: 4px;
  }
  .w {
    max-width: 800px;
    min-width: 600px;
    margin: 0 auto;
  }
  .upload-container {
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 4px;
    margin-top: 40px;
    margin-bottom: 200px;
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
  .uploadbtn-container {
    height: 40px;
    width: 15%;
    margin-right: 5%;
    margin-left: 10%;
    position: relative;
    display: inline-block;
    overflow: hidden;
  }
  .child {
    height: 60px;
    margin: 10px 0;
    display: flex;
  }
  .label {
    width: 15%;
    text-align: left;
    font-size: 14px;
    color: #333;
    margin-right: 5%;
    margin-left: 10%;
    line-height: 40px;
  }
  .input-right {
    width: 30%;
  }
  .input-right.desc {
    width: 50%;
  }
  .child.goods-desc-container {
    height: 90px;
  }
  .goods-img-container {
    margin: 20px 0;
    display: flex;
    max-height: 400px;
    align-items: flex-end;
  }
  .goods-btn-container {
    display: flex;
  }
  .brast {
    margin-left: 50%;
    width: 120px;
  }
  .cancel {
    background: #c2e8fe;
    color: #39b0f7;
    width: 120px;
  }
  .cancel:hover {
    background: #39b0f7;
    color: #fff;
  }
/*  .uploadbtn-container.el-button--primary {
    color: #409EFF;
    border: none;
    background: none;
  }*/
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
