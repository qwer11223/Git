//for...of循环原理，手动调用iterator =============
const set = new Set(['foo', 'bar']);
const iterator = set[Symbol.iterator]();

console.log(iterator.next());
console.log(iterator.next());
console.log(iterator.next());

//iterable对象api分析 ======================
const obj_ = {   //Iterable对象,实现可迭代接口
    [Symbol.iterator]: function () {
        return {    //实现迭代器接口，Iterator
            next: function () {
                return {    //迭代结果接口，IterationResult
                    value: 'aa',
                    done: true
                }
            }
        }
    }
}

//自定义实现iterable函数 ======================
const obj = {
    store: ['foo1', 'bar1'],

    [Symbol.iterator]: function () {
        let index = 0;
        const self = this;

        return {
            next: function () {
                return {
                    value: self.store[index],
                    done: index++ >= self.store.length
                }
            }
        }
    }
}

for (const item of obj) {
    console.log(item);
}

//迭代器模式 ===========================
const todo = {
    life: ['eat', 'sleep'],
    learn: ['chinese', 'math'],

    each: function (callback) {
        const all = [].concat(this.life, this.learn);
        for (const item of all)
            callback(item)
    },

    [Symbol.iterator]: function () {
        const all = [...this.life, ...this.learn];
        let index = 0;
        return {
            next() {
                return {
                    value: all[index],
                    done: index++ >= all.length
                }
            }
        }
    }
}

console.log('------each----------');

todo.each(item => {
    console.log(item);
})

console.log('-------iterable ---------');
for (let item of todo)
    console.log(item);



///////// 几种自定义对象 iterator 的方法

var obj = {
    0: 1,
    1: 2,
    2: 3,
    a: [1, 2, 3, 4],
    length: 3,
    [Symbol.iterator]: function* () {
        //--- 1.自定义 iterator ---//
        // let index = 0
        // let all = [...this.a]
        // return {
        //     next() {
        //         return {
        //             value: all[index],
        //             done: index++ >= all.length
        //         }
        //     }
        // }

        //--- 2.使用 Generator函数 ---//
        for (let t of this.a)
            yield t;
    }
}

//--- 3.直接引用含有iterator的数据类型的Symbol.iterator方法---//
// obj[Symbol.iterator] = Array.prototype[Symbol.iterator]


for (let tmp of obj) {
    console.log(tmp);

}

