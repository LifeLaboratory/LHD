import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/reg',
    name: 'Register',
    component: () => import('../views/Register.vue')
  },
  {
    path: '/start',
    name: 'Start',
    component: () => import('../views/StartGame.vue')
  },
  {
    path: '/choice',
    name: 'Start',
    component: () => import('../views/ChoicePerson.vue')
  },
  {
    path: '/auth',
    name: 'Auth',
    component: () => import('../views/Auth.vue')
  },
  {
    path: '/rating',
    name: 'Rating',
    component: () => import('../views/Rating.vue')
  },
  {
    path: '/game',
    name: 'Game',
    component: () => import('../views/Game.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
