var str = 'demo'

console.log(str)
console.info(str)
console.warn(str)
console.error(str)

const obj = {
    name: 'node.js',
    set: function () {
        console.log('set')
    },
    get: function () {
        console.log('set')
    }
}

console.dir(obj) //讲一个对象的信息输出到控制台



console.time('total_time') //统计一段代码运行时间

console.time('time1')
for (var i = 0; i < 10000; i++) { }
console.timeEnd('time1')
for (var i = 0; i < 10000; i++) { }

console.timeEnd('total_time')

//console.trace('trace')

var arrTable = {
    A: { name: 1 },
    B: { name: 2 },
    C: { name: 3 }
}

console.table(arrTable) //将数组以表格形式输出