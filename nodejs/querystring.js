const querystring = require('querystring')  //查询字符串处理

let str = 'KeyWord=node.js&name=jack'

let obj = querystring.parse(str)

console.log(obj)

let query = {
    KeyWord:'js',
    name:'leo'
}

console.log(querystring.stringify(query))