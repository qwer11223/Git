//Generator避免异步编程中回调嵌套过深问题

// function* foo() {   //生成器函数，内部实现iterator接口
//     console.log('ace');
//     return 100;
// }

// console.log(foo().next());


function* foo() {
    console.log(111);
    yield 100;
    console.log(222);
    yield 200;
    console.log(333);
    yield 300;
}

const generator = foo();
console.log(generator.next());
console.log(generator.next());
console.log(generator.next());
console.log(generator.next());



//生成器应用 =========================

//case1:发号器
function* createIdMaker() {
    let id = 1;
    while (true) {
        yield id++;
    }
}

const idMaker = createIdMaker();

console.log(idMaker.next());
console.log(idMaker.next());
console.log(idMaker.next());
console.log(idMaker.next());
console.log(idMaker.next());
console.log(idMaker.next());


//case2:使用Generator函数实现iterator方法
const todos = {
    life: ['eat', 'sleep'],
    learn: ['chinese', 'math'],
    [Symbol.iterator]: function* () {
        const all = [...this.life, ...this.learn];
        for (const item of all) {
            yield item;
        }
    }
}

for (const item of todos)
    console.log(item);

