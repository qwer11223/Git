/*
const done = 1

const promise = new Promise((resolve, reject) => {

    console.log(1)

    if (done)
        resolve('resolve emit')
    else
        reject("reject emit")
})

console.log(2)

promise.then(resolve => {
    console.log(resolve)
}).catch(err => {
    console.log(err)
}).finally(()=>{
    console.log('finally')
})

console.log(3)

**************/

/*
function timer(ms, num) {
    return new Promise((res, rej) => {
        setTimeout(() => {
            res(num)
        }, ms);
    })
}

timer(1000, 1).then(res => {
    console.log(res)
    return timer(1500, 2)
}).then(res => {
    console.log(res)
    return timer(2000, 3)
}).then(res => {
    console.log(res)
})

*/

async function timer(ms, num) {
    return await new Promise((res, rej) => {
        setTimeout(() => {
            res(num)
        }, ms);
    })
}