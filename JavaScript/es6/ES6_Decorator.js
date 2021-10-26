// [说明] Decorator 提案经过了大幅修改，目前还没有定案，不知道语法会不会再变。下面的内容完全依据以前的提案，已经有点过时了。等待定案以后，需要完全重写。
// 装饰器（Decorator）是一种与类（class）相关的语法，用来注释或修改类和类方法。许多面向对象的语言都有这项功能，目前有一个提案将其引入了 ECMAScript。

@testable
class MyTestableClass {
    // ...
}

function testable(target) {
    target.isTestable = true;
}

MyTestableClass.isTestable // true