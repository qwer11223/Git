// Object.is()
console.log(+0 === -0)
console.log(Object.is(+0, -0))

//Object.assign()
//==
/*
function mixin(receiver,supplier)
{
    Object.keys(supplier).forEach(key=>{
        receiver[key] = supplier[key]
    })
    return receiver
}
*/

function EventTarget() { }
EventTarget.prototype = {
    constructor: EventTarget,
    emit: () => console.log('emit'),
    on: () => console.log('on')
}

var myObject = {}
Object.assign(myObject, EventTarget.prototype)

myObject.on()

//Object.getOwnPropretyNames
var obj = {
    a: 1,
    0: 1,
    c: 1,
    2: 1,
    b: 1,
    1: 1
}

obj.d = 1
console.log(Object.getOwnPropertyNames(obj).join(""))

//change object proptotype

let person = {
    getGreeting() {
        return "Hellow"
    }
}

let dog = {
    getGreeting() {
        return "Woof"
    }
}

//let friend = Object.create(person)

let friend = {
    grtGreeting(){
       // return Object.getPrototypeOf(this).getGreeting.call(this) + ", hi!"
       return super.getGreeting() + ", hi!"
    }
}

Object.setPrototypeOf(friend,person)

console.log(person.getGreeting())


