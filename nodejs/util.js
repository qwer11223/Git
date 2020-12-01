const util = require('util')

let obj = {
    key: 'node',
    value: 'js'
}

console.log(util.inspect(obj, { 'color': true })) //对象反序列化


console.log(util.format('%s and %d','aa',1))
console.log(util.format('%s and %d','aa',1,2))
console.log(util.format('%s and %d %d','aa',1))
console.log(util.format('ss','aa',1))

//判断数据类型
//util.isArray() ...