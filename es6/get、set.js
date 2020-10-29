//与 ES5 一样， 在 Class 内部可以使用get和set关键字， 对某个属性设置存值函数和取值函数， 拦截该属性的存取行为

let obj ={
    a:1,

    set prop(value){
        console.log('setValue:'+ value)
    },

    get prop(){
        return 'aaa'
    }
}

//console.log(obj.prop)

obj.prop = 10