import { createRouter, createWebHistory } from "vue-router";

// pages
import App from './App.vue';


const routes = [
    {path: '/', component: App},
    {path: '/two', component: <h1>HELLO</h1>},
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router