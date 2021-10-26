//object deconstruction
let node = {
    type: "Indetifier",
    name: "foo"
}

let { type, name, age = 30 } = node

console.log(type, name, age)

//destructuring assignment

let type1 = "Literal", name1 = 5;

({ type: type1, name: name1 } = node)

console.log(type1, name1)

//nesting object deconstruction
let nest = {
    type: "Indetifier",
    name: "foo",
    loc: {
        start: {
            line: 1,
            column: 4,
            end: {
                line: 1,
                column: 1
            }
        },

    },
    range: [0, 1]
}

let { loc: { start: { end } } } = nest

console.log(end.line, end.column)

//mixin deconstruction

let { loc: { start }, range: [Index] } = nest

console.log(start.line, Index)


/************* array ***************/

//array deconstruction
let colors = ["red", "green", "blue"]

let [firstColor, secondColor] = colors

console.log(firstColor, secondColor)

let [, , thirdColor] = colors
console.log(thirdColor)

//change value
let a = 1, b = 2;

[a, b] = [b, a]
console.log("a=" + a, "b=" + b)

//nesting array deconstruction
let nums = ["one", ["two", "three"], "four"]

let num = [firstNum, [secondNum]] = nums

console.log(firstNum, secondNum)

let [...clonedNums] = nums

console.log(clonedNums)