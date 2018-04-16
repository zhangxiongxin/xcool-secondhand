import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@/pages/home'
import Add from '@/pages/home/createItem'
import Login from '@/pages/login'
import Register from '@/pages/register'
import NotFound from '@/pages/404'

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
      path: '/add',
      name: 'add',
      component: Add
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
