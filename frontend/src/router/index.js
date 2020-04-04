import Vue from 'vue'
import Router from 'vue-router'

const routerOptions = [
  {
    path: '/', name: 'Home', component: 'Home'
  },
  {
    path: '/about', name: 'About', component: 'About'
  },
  {
    path: '/contact', name: 'Contact', component: 'Contact'
  },
  {
    path: '/projects', name: 'Projects', component: 'Projects'
  },
  {
    path: '/newproject', name: 'NewProject', component: 'NewProject'
  },
  {
    path: '*', name: 'notfound', component: 'NotFound'
  }
]

const routes = routerOptions.map (route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})

Vue.use(Router)

export default new Router({
  routes,
  mode : 'history'
})
