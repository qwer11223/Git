import VueRouter from "vue-router"

import account from "./main/account.vue"
import list from "./main/list.vue"
import login from "./subcom/login.vue"
import register from "./subcom/register.vue"



var router = new VueRouter({
    routes: [
        {
            path: '/account',
            component: account,
            children: [
                { path: 'login', component: login },
                { path: 'register', component: register },
            ]
        },
        { path: '/list', component: list }
    ]
})

export default router