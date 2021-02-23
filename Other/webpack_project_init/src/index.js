import m1 from "./m1.js"

import "./index.css"
import "./1.scss"
import App from "./App.vue";
import Vue from "vue"
import VueRouter from "vue-router"
Vue.use(VueRouter)

import MintUi from "mint-ui"
import 'mint-ui/lib/style.css'

Vue.use(MintUi)

import router from "./router.js"





var vm = new Vue({
    el: '.app',
    data: {
        msg: 1233
    },
    render: c => c(App),
    router
})

console.log(m1.a)

