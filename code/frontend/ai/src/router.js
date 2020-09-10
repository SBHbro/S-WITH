import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import ToHandLan from './views/HandLan/ToHandLan.vue'
import FromHandLan from './views/HandLan/FromHandLan.vue'
import FromHandLanResult from './views/HandLan/FromHandLanResult.vue'
import ToHandLanResult from './views/HandLan/ToHandLanResult.vue'

Vue.use(Router) //플러그인 등록

export default new Router({
    routes: [
        {
            path: '/',
            name: 'Home',
            component: Home,
        },
        {
            path: '/toHandLan',
            name: 'ToHandLan',
            component: ToHandLan,
        },
        {
            path: '/fromHandLan',
            name: 'FromHandLan',
            component: FromHandLan,
        },
        {
            path: '/fromHandLanResult',
            name: 'FromHandLanResult',
            component: FromHandLanResult,
        },
        {
            path: '/toHandLanResult',
            name: 'ToHandLanResult',
            component: ToHandLanResult,
        },
    ]
})