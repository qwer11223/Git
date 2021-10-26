// js five iterative methods
// every、 some、 filter、 map、 foreach

// array.every(function(currentValue,index,arr), thisValue)

var arr = [32, 25, 26, 10, 39]

//不能跳出循环
//forEach() 方法用于调用数组的每个元素，并将元素传递给回调函数。
arr.forEach(function (vaule) {
    console.log(vaule)
})

//返回false终止循环
//every 如果数组中检测到有一个元素不满足，则整个表达式返回 false ，且剩余的元素不会再进行检测。
console.log(
    arr.every(function (vaule) {
        return vaule < 30
    })
)

//返回true终止循环
//some 如果有一个元素满足条件，则表达式返回true , 剩余的元素不会再执行检测。
console.log(
    arr.some(function (vaule) {
        return vaule < 30
    })
)

//filter() 方法创建一个新的数组，新数组中的元素是通过检查指定数组中符合条件的所有元素。
console.log(
    arr.filter(function (vaule) {
        return vaule < 30
    })
)

//map() 方法返回一个新数组，数组中的元素为原始数组元素调用函数处理后的值。
console.log(
    arr.map(function (vaule) {
        return vaule / 10
    })
)

