//Symbol类型是为了解决属性名冲突的问题，顺带还具备模拟私有属性的功能。

/*
创建symbol变量最简单的方法是用Symbol()函数。symbol变量有两点比较特别：

1.它可以作为对象属性名。只有字符串和 symbol 类型才能用作对象属性名。
2.没有两个symbol 的值是相等的。
*/

// 注意：使用Symbol值定义属性时，必须放在方括号中
// 原因：点运算符后总是字符串，所以不会读取Symbol作为标识名所指代的值

let s = Symbol()
console.log(typeof s);

var name = Symbol();
var obj = {
    [name]: '132',
    getName() {
        console.log(this[name]); //Symbol模拟私有属性
    }
}
obj.getName();
console.log(obj.name);
console.log(Object.getOwnPropertySymbols(obj)); //通过该方法才能获取对象的symbol属性


//获取相同的Symbol
const s1 = Symbol.for('foo');
const s2 = Symbol.for('foo');
console.log(s1 === s2);
