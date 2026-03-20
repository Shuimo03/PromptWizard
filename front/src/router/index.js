import { createRouter, createWebHistory } from 'vue-router'
import PromptGenerator from '../components/PromptGenerator.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: PromptGenerator,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
