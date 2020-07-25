import m1 from "./m1.js"

import "./index.css"
import "./1.scss"
import login from "./1.vue";

import Vue from "vue"

var vm = new Vue({
    el:'.app',
    data:{
        msg:1233
    },
    render:c=>c(login)
})

console.log(m1.a)

