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
import Profile from '@/pages/home/profile'
import Emain from '@/pages/admin/main'
import AdminLogin from '@/pages/admin/login'
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
      path: '/adminLogin',
      name: 'adminLogin',
      component: AdminLogin
    },
    {
      path: '/admin',
      name: 'admin',
      redirect: '/admin/adminLogin',
      component: Admin,
      children: [
        {
          path: 'main',
          name: 'emain',
          component: Emain
        },
        {
          path: 'adminLogin',
          name: 'adminLogin',
          component: AdminLogin
        }
      ]
    },
    {
      path: '/add',
      name: 'add',
      component: Add
    },
    {
      path: '/profile',
      name: 'profile',
      component: Profile
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
