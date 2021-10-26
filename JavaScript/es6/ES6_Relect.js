//Reflect 可以用于获取目标对象的行为，它与 Object 类似，但是更易读，为操作对象提供了一种更优雅的方式。

const obj = {
    name: 'jack',
    age: 20
}

console.log(Reflect.has(obj, 'name'));
console.log(Reflect.deleteProperty(obj, 'age'));
console.log(Reflect.ownKeys(obj));
