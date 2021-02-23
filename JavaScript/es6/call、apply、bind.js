//call()、apply()、bind()是用来改变this的指向的

//call 、bind 、 apply 这三个函数的第一个参数都是 this 的指向对象
//bind返回函数

var obj = {
    name: 'jack',
    objAge: this.age,
    fun: function (arg1, arg2) {
        console.log(this.name + ' ' + this.age + ' ' + arg1 + ' ' + arg2)
    }
}

var db = {
    name: 'leo',
    age: 21
}

obj.fun.call(db, 1,2)
obj.fun.apply(db, [1,2])
obj.fun.bind(db, 1,2)()
// =
//var defFun = obj.fun.bind(db,1)
//defFun()