//ES6的类可以看作只是一个语法糖，让原型对象写法跟清晰、更像面向对象编程语法而已，完全可以看做构造函数的另一种写法。

class Point {
    //...
}

console.log(typeof Point); //'function'
console.log(Point === Point.prototype.constructor); //true



