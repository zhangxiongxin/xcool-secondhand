export let checkType = (() => {
  let rules = {
    email (str) {
      return /^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$/.test(str)
    },
    mobile (str) {
      return /^1[0-9]{10}$/.test(str)
    },
    tel (str) {
      return /^(0\d{2,3}-\d{7,8})(-\d{1,4})?$/.test(str)
    },
    number (str) {
      return /^[0-9]$/.test(str)
    },
    english (str) {
      return /^[a-zA-Z]+$/.test(str)
    },
    text (str) {
      return /^\w+$/.test(str)
    },
    chinese (str) {
      return /^[\u4E00-\u9FA5]+$/.test(str)
    },
    lower (str) {
      return /^[a-z]+$/.test(str)
    },
    upper (str) {
      return /^[A-Z]+$/.test(str)
    }
  }
  return {
    check (str, type) {
      return rules[type] ? rules[type](str) : false
    },
    addRule (type, fn) {
      rules[type] = fn
    }
  }
})()
