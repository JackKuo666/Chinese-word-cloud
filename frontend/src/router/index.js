import Vue from 'vue'
import Router from 'vue-router'
// eslint-disable-next-line no-unused-vars
import WordCloud from '../WordCloud'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: WordCloud
    }
  ]
})
