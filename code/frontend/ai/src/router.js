import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import ToHandLan from './views/HandLan/ToHandLan.vue'
import FromHandLan from './views/HandLan/FromHandLan.vue'
<<<<<<< HEAD
import Board from './views/board/Board.vue'
import BoardCreate from './views/board/BoardCreate.vue'
import BoardDetail from './views/board/BoardDetail.vue'
import BoardUpdate from './views/board/BoardUpdate.vue'
import Camera from './views/Camera.vue'


=======
import FromHandLanResult from './views/HandLan/FromHandLanResult.vue'
>>>>>>> 505e42ad00bf7f3e02f4a7eaf1015eed99dcfba9

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
<<<<<<< HEAD
            path: '/board',
            name: 'Board',
            component: Board,
        },
        {
            path: '/board/create',
            name: 'BoardCreate',
            component: BoardCreate,
        },
        {
            path: '/board/detail',
            name: 'BoardDetail',
            component: BoardDetail,
        },
        {
            path: '/board/update',
            name: 'BoardUpdate',
            component: BoardUpdate,
        },
        {
            path: '/camera',
            name: 'Camera',
            component: Camera,
=======
            path: '/fromHandLanResult',
            name: 'FromHandLanResult',
            component: FromHandLanResult,
>>>>>>> 505e42ad00bf7f3e02f4a7eaf1015eed99dcfba9
        },
    ]
})