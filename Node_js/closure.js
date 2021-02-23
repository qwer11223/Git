var str = 'node'

function copy() {

    var str2 = str

    return function(){
        console.log(str2)
    }
}

copy()()