//proxy 可在目标对象前架设一"拦截"层，对外界访问进行过滤和改写

var person = {
    name: 'jack'
}

var obj = new Proxy(person, {
    get: function (target, property) {
        if(property in target)
            return target[property]
        else
            throw new ReferenceError(`Property ${property} does not exist`)
    }
})

console.log(obj.name);
