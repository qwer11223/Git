let values = [10, 20, 30]

console.log(Math.max(...values))

    ; (function fun(num) {
        console.log(num)
    })(5)

function Pro(arg1, arg2) {
    this.arg1 = arg1
    this.arg2 = arg2
}

var pro1 = new Pro(1, 2);

console.log(pro1)

var demoFun = {
    a: 'demo',

    set b(x) {
        b = x
    },

    get b() {
        return b
    },

    fun: function () {
        console.log(1)
    }

}

var newFun = function(){
    console.log(2)
}

console.log(newFun.bind().name)