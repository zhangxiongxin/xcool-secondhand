import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@/pages/home'
import Add from '@/pages/home/createItem'
import Login from '@/pages/login'
import Register from '@/pages/register'
import NotFound from '@/pages/404'
import Pay from '@/pages/home/pay'
import Admin from '@/pages/admin'
import Detail from '@/pages/home/detail'
Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage
    },
    {
      path: '/admin',
      name: 'admin',
      component: Admin
    },
    {
      path: '/add',
      name: 'add',
      component: Add
    },
    {
      path: '/detail',
      name: 'detail',
      component: Detail
    },
    {
      path: '/pay',
      name: 'pay',
      component: Pay
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '*',
      name: 'notFound',
      component: NotFound
    }
  ]
})
