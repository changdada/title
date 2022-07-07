import Vue from 'vue'
import VueRouter from 'vue-router'

import index from '../views/index'//主页
import Homepage from '../views/Homepage' //历史记录
import Login from "../views/Login" //登陆
import Register from "../views/Register"; //注册
import Title from "../views/Title"; //生成页面
import User from "../views/User"; //个人信息
import Power from "../views/power"; //能力介绍
import Help from "../views/help"; //帮助文档

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'index',
    component: index,
    meta:{
      // 页面标题title
      title: '智能创作平台'
    }
  },
  {
    path: '/index',
    name: 'index',
    component: index,
    meta:{
      // 页面标题title
      title: '智能创作平台'
    }
  },
  {
        path: '/Login',
        name: 'login',
        component: Login,
    meta:{
      // 页面标题title
      title: '智能创作平台'
    }
    },
    {
        path: '/Register',
        name: 'Register',
        component: Register,
      meta:{
        // 页面标题title
        title: '智能创作平台'
      }
    }, {
        path: '/Homepage',
        name: 'Homepage',
        component: Homepage,
    meta:{
      // 页面标题title
      title: '智能创作平台'
    }
    },
  {
    path: '/Title',
    name: 'Title',
    component: Title,
    meta:{
      // 页面标题title
      title: '智能创作平台'
    }
  },
  {
    path: '/User',
    name: 'User',
    component: User,
    meta:{
      // 页面标题title
      title: '智能创作平台'
    }
  },
  {
    path: '/Help',
    name: 'Help',
    component: Help,
    meta:{
      // 页面标题title
      title: '智能创作平台'
    }
  },
  {
    path: '/Power',
    name: 'Power',
    component: Power,
    meta:{
      // 页面标题title
      title: '智能创作平台'
    }
  },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
